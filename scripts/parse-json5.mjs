import fs from 'node:fs'
import JSON5 from 'json5'
const inputs = JSON.parse(fs.readFileSync(0, 'utf8'))
process.stdout.write(JSON.stringify(inputs.map(text => {
  try { return { value: JSON5.parse(text.replace(/^\uFEFF/, '')) } }
  catch (error) { return { error: error.message } }
})))
