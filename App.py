# importing libraries
import random
import webbrowser


# list containing all 150 problems - I know this is painful but shush
problems = [
    'contains-duplicate', 'valid-anagram', 'two-sum', 'group-anagrams', 'top-k-frequent-elements',
    'encode-and-decode-strings', 'product-of-array-except-self', 'valid-sudoku', 'longest-consecutive-sequence',
    'valid-palindrome', 'two-sum-ii-input-array-is-sorted', '3sum', 'container-with-most-water', 'trapping-rain-water',
    'best-time-to-buy-and-sell-stock', 'longest-substring-without-repeating-characters',
    'longest-repeating-character-replacement', 'permutation-in-string', 'minimum-window-substring',
    'sliding-window-maximum', 'valid-parentheses', 'min-stack', 'evaluate-reverse-polish-notation',
    'generate-parentheses', 'daily-temperatures', 'car-fleet', 'largest-rectangle-in-histogram',
    'binary-search', 'search-a-2d-matrix', 'koko-eating-bananas', 'find-minimum-in-rotated-sorted-array',
    'search-in-rotated-sorted-array', 'time-based-key-value-store', 'median-of-two-sorted-arrays',
    'reverse-linked-list', 'merge-two-sorted-lists', 'reorder-list', 'remove-nth-node-from-end-of-list',
    'copy-list-with-random-pointer', 'add-two-numbers', 'linked-list-cycle', 'find-the-duplicate-number',
    'lru-cache', 'merge-k-sorted-lists', 'reverse-nodes-in-k-group', 'invert-binary-tree',
    'maximum-depth-of-binary-tree', 'balanced-binary-tree', 'same-tree', 'subtree-of-another-tree',
    'lowest-common-ancestor-of-a-binary-search-tree', 'binary-tree-level-order-traversal',
    'binary-tree-right-side-view', 'count-good-nodes-in-binary-tree', 'validate-binary-search-tree',
    'kth-smallest-element-in-a-bst', 'construct-binary-tree-from-preorder-and-inorder-traversal',
    'binary-tree-maximum-path-sum', 'serialize-and-deserialize-binary-tree', 'kth-largest-element-in-s-stream',
    'last-stone-weight', 'k-closest-points-to-origin', 'kth-largest-elements-in-an-array', 'task-scheduler',
    'design-twitter', 'find-median-from-data-stream', 'subsets', 'combination-sum', 'permutations', 'subsets-ii',
    'combination-sum-ii', 'word-search', 'palindrome-partitioning', 'letter-combination-of-a-phone-number',
    'n-queens', 'implement-trie-prefix-tree', 'design-add-and-search-words-data-structure', 'word-search-ii',
    'number-of-islands', 'max-area-of-island', 'clone-graph', 'walls-and-gates', 'rotting-oranges',
    'pacific-atlantic-water-flow', 'surrounded-regions', 'course-schedule', 'course-schedule-ii',
    'graph-valid-tree', 'number-of-connected-components-in-an-undirected-graph', 'redundant-connection',
    'word-ladder', 'reconstruct-itinerary', 'min-cost-to-connect-all-points', 'network-delay-time',
    'swim-in-rising-water', 'alien-dictionary', 'cheapest-flights-with-k-stops', 'climbing-stairs',
    'min-cost-climbing-stairs', 'house-robber', 'house-robber-ii', 'longest-palindromic-substring',
    'palindromic-substrings', 'decode-ways', 'coin-change', 'maximum-product-subarray', 'word-break',
    'longest-increasing-subsequence', 'partition-equal-subset-sum', 'unique-paths',
    'longest-common-subsequence', 'best-time-to-buy-and-sell-stock-with-cooldown', 'coin-change-ii',
    'target-sum', 'interleaving-string', 'longest-increasing-path-in-a-matrix', 'distinct-subsequences',
    'edit-distance', 'burst-balloons', 'regular-expression-matching', 'maximum-subarray', 'jump-game',
    'jump-game-ii', 'gas-station', 'hand-of-straights', 'merge-triplets-to-form-target-triplet',
    'partition-labels', 'valid-parenthesis-string', 'insert-interval', 'merge-intervals',
    'non-overlapping-intervals', 'meeting-rooms', 'meeting-rooms-ii', 'minimum-interval-to-include-each-query',
    'rotate-image', 'spiral-matrix', 'set-matrix-zeroes', 'happy-number', 'plus-one', 'powx-n',
    'multiply-strings', 'detect-squares', 'single-number', 'number-of-1-bits', 'counting-bits', 'reverse-bits',
    'missing-number', 'sum-of-two-integers', 'reverse-integer'
]


# picking random item from above list
index = random.randint(0, 149)


# printing result to console and redirecting user to page
print("generated problem: " + problems[index])
link = "https://leetcode.com/problems/" + problems[index] + "/"
webbrowser.open(link)
