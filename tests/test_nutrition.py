import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'scripts'))
from nutrition_catalogue import expand_variants, resolve, profile_for, composition, combine, patch_assets


class NutritionTests(unittest.TestCase):
    def test_property_loaded_variants_and_exclusions(self):
        props = {('game', 'plant/fruit'): {'code': 'fruit', 'variants': [{'code': 'apple'}, {'code': 'pear'}]}}
        obj = {'code': 'fruit', 'variantgroups': [{'loadFromProperties': 'plant/fruit'}, {'code': 'state', 'states': ['raw', 'dried']}], 'skipVariants': ['*-pear-dried']}
        rows, missing = expand_variants(obj, 'game', props)
        self.assertEqual([r[0] for r in rows], ['fruit-apple-raw', 'fruit-apple-dried', 'fruit-pear-raw'])
        self.assertFalse(missing)

    def test_first_matching_branch_merges_and_nested_placeholders(self):
        obj = {'attributes': {'tags': ['base']}, 'attributesByType': {'*-apple': {'tags': ['fruit'], 'label': '{type}'}, '*': {'label': 'wrong'}}}
        row = resolve(obj, 'fruit-apple', {'type': 'apple'})
        self.assertEqual(row['attributes'], {'tags': ['base', 'fruit'], 'label': 'apple'})

    def test_exact_profile_beats_prefix(self):
        config = {'Foods': [{'Codes': ['game:fruit-*']}, {'Codes': ['game:fruit-apple']}]}
        self.assertEqual(profile_for('game:fruit-apple', config)[1], 1)
        self.assertEqual(profile_for('game:fruit-pear', config)[1], 0)

    def test_cooking_retains_minerals_and_halves_vitamin_c(self):
        p = {'PortionG': 100, 'Preparation': 'raw', 'WaterGPer100G': 80, 'Per100G': {'carbohydrate': 10, 'protein': 1, 'fat': 0, 'fiber': 2}, 'MicroPer100G': {'ironMg': 3, 'vitaminCMg': 20}}
        d = composition(p, cooked=True)
        self.assertEqual(d['values']['ironMg'], 3)
        self.assertEqual(d['values']['vitaminCMg'], 10)
        self.assertAlmostEqual(d['values']['energy'], 11*16.736)
        self.assertNotIn('b12Ug', d['values'])

    def test_fallback_uses_satiety_and_does_not_invent_micros(self):
        p = {'PortionG': 0, 'WaterGPer100G': 0, 'Per100G': {'carbohydrate': 100}, 'MicroPer100G': {'ironMg': 5}}
        d = composition(p, {'satiety': 200}, mapped=False)
        self.assertAlmostEqual(d['mass'], 50)
        self.assertNotIn('ironMg', d['values'])

    def test_unknown_ingredient_stays_unknown(self):
        result = combine([{'mass': 100, 'values': {'protein': 5, 'ironMg': 2}}, {'mass': 100, 'values': {'protein': 3}}])
        self.assertEqual(result['values'], {'protein': 8})

    def test_patches_obey_dependencies_and_disabled_state(self):
        parsed = [dict(file='assets/game/itemtypes/food/test.json', domain='game', mod='game', data={'nutritionProps': {'satiety': 1}}),
                  dict(file='assets/addon/patches/foods.json', domain='addon', mod='addon', data=[
                      {'file': 'game:itemtypes/food/test.json', 'op': 'replace', 'path': '/nutritionProps/satiety', 'value': 10},
                      {'file': 'game:itemtypes/food/test.json', 'op': 'replace', 'path': '/nutritionProps/satiety', 'value': 20, 'dependsOn': [{'modid': 'missing'}]},
                      {'file': 'game:itemtypes/food/test.json', 'op': 'replace', 'path': '/nutritionProps/satiety', 'value': 30, 'enabled': False}])]
        assets, summary = patch_assets(parsed, [])
        self.assertEqual(assets[0]['data']['nutritionProps']['satiety'], 10)
        self.assertEqual(summary['pending'], 0)


if __name__ == '__main__': unittest.main()
