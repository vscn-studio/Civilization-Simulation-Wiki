// Display names only. Original identifiers and downloaded data remain unchanged.
export const nutrients = {
  carbohydrate:['碳水化合物','g'], protein:['蛋白质','g'], fat:['脂肪','g'], fiber:['膳食纤维','g'],
  calciumMg:['钙','mg'], ironMg:['铁','mg'], zincMg:['锌','mg'], vitaminAUgRAE:['维生素 A（视黄醇活性当量）','μg'],
  vitaminCMg:['维生素 C','mg'], b1Mg:['维生素 B₁','mg'], b6Mg:['维生素 B₆','mg'],
  folateUgDFE:['叶酸（膳食叶酸当量）','μg'], b12Ug:['维生素 B₁₂','μg']
}
export const categories = { Fruit:'水果', Vegetable:'蔬菜', Protein:'蛋白质类', Grain:'谷物', Dairy:'乳品', NoNutrition:'不属于原版营养类别', Unknown:'未知', '—':'未声明' }
export const preparations = { raw:'生食／未加热', cooked:'熟制', baked:'烘烤', smoked:'烟熏', dried:'干燥', cured:'盐腌', liquid:'液体', fermented:'发酵', roasted:'烤制' }
export const confidence = { high:'高', medium:'中', low:'低' }
export const formatNumber = value => value == null ? '未声明' : typeof value === 'number' ? new Intl.NumberFormat('zh-CN', { maximumFractionDigits:3 }).format(value) : value
