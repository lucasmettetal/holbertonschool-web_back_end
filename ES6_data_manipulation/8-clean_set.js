export default function cleanSet(set, startString) {
  const result = [];
  for (const val of set) {
    if (typeof val === 'string' && val.startsWith(startString)) {
      result.push(val.slice(startString.length));
    }
  }
  return result.join('-');
}
