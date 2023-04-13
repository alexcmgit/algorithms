/**
 * @param {string} source
 * @return {number}
 */
function lengthOfLongestSubstring(source) {
  let current = ""
  const sequences = []

  for (let i = 0; i < source.length; i++) {
    current += source[i]

    for (let j = i + 1; j < source.length; j++) {
      if (current.includes(source[j])) {
        break
      } else {
        current += source[j]
      }
    }

    sequences.push(current)
    current = ""
  }

  return (sequences.sort((a, z) => z.length - a.length)[0] || "").length
}

module.exports = lengthOfLongestSubstring