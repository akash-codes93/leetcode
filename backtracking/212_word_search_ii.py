"""
https://leetcode.com/problems/word-search-ii/
"""


class Node:

    def __init__(self, val, ends_here=False):
        self.val = val
        self.ends_here = ends_here
        self.next_chars = [None] * 26


class Trie:

    def __init__(self):
        self.base = Node('/')

    def insert(self, word):
        tr = self.base
        i = 0
        while i < len(word):
            idx = ord(word[i]) - 97
            if tr.next_chars[idx] is None:
                node = Node(word[i])
                tr.next_chars[idx] = node
            else:
                node = tr.next_chars[idx]

            if i == len(word) - 1:
                node.ends_here = True

            tr = node
            i = i + 1

    def search(self, word):
        tr = self.base
        i = 0
        while i < len(word):
            idx = ord(word[i]) - 97
            # print(word[i], idx)
            if tr.next_chars[idx] is None:
                return False
            tr = tr.next_chars[idx]
            i += 1

        if tr.ends_here == True:
            return True
        return False


class Solution:
    def findWords(self, board: List[List[str]], wordDict: List[str]) -> List[str]:

        m = len(board)
        n = len(board[0])

        output = set()
        trie = Trie()
        for _w in wordDict:
            trie.insert(_w)

        # wordDict = set(wordDict)

        def find_paths(i, j):
            paths = []

            if j + 1 < n and board[i][j + 1] != '$':
                paths.append((i, j + 1))

            if i + 1 < m and board[i + 1][j] != '$':
                paths.append((i + 1, j))

            if i - 1 >= 0 and board[i - 1][j] != '$':
                paths.append((i - 1, j))

            if j - 1 >= 0 and board[i][j - 1] != '$':
                paths.append((i, j - 1))

            return paths

        def dfs(i, j, word):
            word += board[i][j]
            board[i][j] = '$'
            val = trie.search(word)
            # print(val, word)
            if val:
                output.add(word)
                if len(output) == len(wordDict):
                    board[i][j] = word[-1]
                    return

            paths = find_paths(i, j)

            for path in paths:
                dfs(path[0], path[1], word)

            board[i][j] = word[-1]
            word = word[:-1]

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                dfs(i, j, "")
                if len(output) == len(wordDict):
                    break
        return list(output)


"""
Reverse check this is also not working 
[["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"]]
["ababababaa","ababababab","ababababac","ababababad","ababababae","ababababaf","ababababag","ababababah","ababababai","ababababaj","ababababak","ababababal","ababababam","ababababan","ababababao","ababababap","ababababaq","ababababar","ababababas","ababababat","ababababau","ababababav","ababababaw","ababababax","ababababay","ababababaz","ababababba","ababababbb","ababababbc","ababababbd","ababababbe","ababababbf","ababababbg","ababababbh","ababababbi","ababababbj","ababababbk","ababababbl","ababababbm","ababababbn","ababababbo","ababababbp","ababababbq","ababababbr","ababababbs","ababababbt","ababababbu","ababababbv","ababababbw","ababababbx","ababababby","ababababbz","ababababca","ababababcb","ababababcc","ababababcd","ababababce","ababababcf","ababababcg","ababababch","ababababci","ababababcj","ababababck","ababababcl","ababababcm","ababababcn","ababababco","ababababcp","ababababcq","ababababcr","ababababcs","ababababct","ababababcu","ababababcv","ababababcw","ababababcx","ababababcy","ababababcz","ababababda","ababababdb","ababababdc","ababababdd","ababababde","ababababdf","ababababdg","ababababdh","ababababdi","ababababdj","ababababdk","ababababdl","ababababdm","ababababdn","ababababdo","ababababdp","ababababdq","ababababdr","ababababds","ababababdt","ababababdu","ababababdv","ababababdw","ababababdx","ababababdy","ababababdz","ababababea","ababababeb","ababababec","ababababed","ababababee","ababababef","ababababeg","ababababeh","ababababei","ababababej","ababababek","ababababel","ababababem","ababababen","ababababeo","ababababep","ababababeq","ababababer","ababababes","ababababet","ababababeu","ababababev","ababababew","ababababex","ababababey","ababababez","ababababfa","ababababfb","ababababfc","ababababfd","ababababfe","ababababff","ababababfg","ababababfh","ababababfi","ababababfj","ababababfk","ababababfl","ababababfm","ababababfn","ababababfo","ababababfp","ababababfq","ababababfr","ababababfs","ababababft","ababababfu","ababababfv","ababababfw","ababababfx","ababababfy","ababababfz","ababababga","ababababgb","ababababgc","ababababgd","ababababge","ababababgf","ababababgg","ababababgh","ababababgi","ababababgj","ababababgk","ababababgl","ababababgm","ababababgn","ababababgo","ababababgp","ababababgq","ababababgr","ababababgs","ababababgt","ababababgu","ababababgv","ababababgw","ababababgx","ababababgy","ababababgz","ababababha","ababababhb","ababababhc","ababababhd","ababababhe","ababababhf","ababababhg","ababababhh","ababababhi","ababababhj","ababababhk","ababababhl","ababababhm","ababababhn","ababababho","ababababhp","ababababhq","ababababhr","ababababhs","ababababht","ababababhu","ababababhv","ababababhw","ababababhx","ababababhy","ababababhz","ababababia","ababababib","ababababic","ababababid","ababababie","ababababif","ababababig","ababababih","ababababii","ababababij","ababababik","ababababil","ababababim","ababababin","ababababio","ababababip","ababababiq","ababababir","ababababis","ababababit","ababababiu","ababababiv","ababababiw","ababababix","ababababiy","ababababiz","ababababja","ababababjb","ababababjc","ababababjd","ababababje","ababababjf","ababababjg","ababababjh","ababababji","ababababjj","ababababjk","ababababjl","ababababjm","ababababjn","ababababjo","ababababjp","ababababjq","ababababjr","ababababjs","ababababjt","ababababju","ababababjv","ababababjw","ababababjx","ababababjy","ababababjz","ababababka","ababababkb","ababababkc","ababababkd","ababababke","ababababkf","ababababkg","ababababkh","ababababki","ababababkj","ababababkk","ababababkl","ababababkm","ababababkn","ababababko","ababababkp","ababababkq","ababababkr","ababababks","ababababkt","ababababku","ababababkv","ababababkw","ababababkx","ababababky","ababababkz","ababababla","abababablb","abababablc","ababababld","abababable","abababablf","abababablg","abababablh","ababababli","abababablj","abababablk","ababababll","abababablm","ababababln","abababablo","abababablp","abababablq","abababablr","ababababls","abababablt","abababablu","abababablv","abababablw","abababablx","abababably","abababablz","ababababma","ababababmb","ababababmc","ababababmd","ababababme","ababababmf","ababababmg","ababababmh","ababababmi","ababababmj","ababababmk","ababababml","ababababmm","ababababmn","ababababmo","ababababmp","ababababmq","ababababmr","ababababms","ababababmt","ababababmu","ababababmv","ababababmw","ababababmx","ababababmy","ababababmz","ababababna","ababababnb","ababababnc","ababababnd","ababababne","ababababnf","ababababng","ababababnh","ababababni","ababababnj","ababababnk","ababababnl","ababababnm","ababababnn","ababababno","ababababnp","ababababnq","ababababnr","ababababns","ababababnt","ababababnu","ababababnv","ababababnw","ababababnx","ababababny","ababababnz","ababababoa","ababababob","ababababoc","ababababod","ababababoe","ababababof","ababababog","ababababoh","ababababoi","ababababoj","ababababok","ababababol","ababababom","ababababon","ababababoo","ababababop","ababababoq","ababababor","ababababos","ababababot","ababababou","ababababov","ababababow","ababababox","ababababoy","ababababoz","ababababpa","ababababpb","ababababpc","ababababpd","ababababpe","ababababpf","ababababpg","ababababph","ababababpi","ababababpj","ababababpk","ababababpl","ababababpm","ababababpn","ababababpo","ababababpp","ababababpq","ababababpr","ababababps","ababababpt","ababababpu","ababababpv","ababababpw","ababababpx","ababababpy","ababababpz","ababababqa","ababababqb","ababababqc","ababababqd","ababababqe","ababababqf","ababababqg","ababababqh","ababababqi","ababababqj","ababababqk","ababababql","ababababqm","ababababqn","ababababqo","ababababqp","ababababqq","ababababqr","ababababqs","ababababqt","ababababqu","ababababqv","ababababqw","ababababqx","ababababqy","ababababqz","ababababra","ababababrb","ababababrc","ababababrd","ababababre","ababababrf","ababababrg","ababababrh","ababababri","ababababrj","ababababrk","ababababrl","ababababrm","ababababrn","ababababro","ababababrp","ababababrq","ababababrr","ababababrs","ababababrt","ababababru","ababababrv","ababababrw","ababababrx","ababababry","ababababrz","ababababsa","ababababsb","ababababsc","ababababsd","ababababse","ababababsf","ababababsg","ababababsh","ababababsi","ababababsj","ababababsk","ababababsl","ababababsm","ababababsn","ababababso","ababababsp","ababababsq","ababababsr","ababababss","ababababst","ababababsu","ababababsv","ababababsw","ababababsx","ababababsy","ababababsz","ababababta","ababababtb","ababababtc","ababababtd","ababababte","ababababtf","ababababtg","ababababth","ababababti","ababababtj","ababababtk","ababababtl","ababababtm","ababababtn","ababababto","ababababtp","ababababtq","ababababtr","ababababts","ababababtt","ababababtu","ababababtv","ababababtw","ababababtx","ababababty","ababababtz","ababababua","ababababub","ababababuc","ababababud","ababababue","ababababuf","ababababug","ababababuh","ababababui","ababababuj","ababababuk","ababababul","ababababum","ababababun","ababababuo","ababababup","ababababuq","ababababur","ababababus","ababababut","ababababuu","ababababuv","ababababuw","ababababux","ababababuy","ababababuz","ababababva","ababababvb","ababababvc","ababababvd","ababababve","ababababvf","ababababvg","ababababvh","ababababvi","ababababvj","ababababvk","ababababvl","ababababvm","ababababvn","ababababvo","ababababvp","ababababvq","ababababvr","ababababvs","ababababvt","ababababvu","ababababvv","ababababvw","ababababvx","ababababvy","ababababvz","ababababwa","ababababwb","ababababwc","ababababwd","ababababwe","ababababwf","ababababwg","ababababwh","ababababwi","ababababwj","ababababwk","ababababwl","ababababwm","ababababwn","ababababwo","ababababwp","ababababwq","ababababwr","ababababws","ababababwt","ababababwu","ababababwv","ababababww","ababababwx","ababababwy","ababababwz","ababababxa","ababababxb","ababababxc","ababababxd","ababababxe","ababababxf","ababababxg","ababababxh","ababababxi","ababababxj","ababababxk","ababababxl","ababababxm","ababababxn","ababababxo","ababababxp","ababababxq","ababababxr","ababababxs","ababababxt","ababababxu","ababababxv","ababababxw","ababababxx","ababababxy","ababababxz","ababababya","ababababyb","ababababyc","ababababyd","ababababye","ababababyf","ababababyg","ababababyh","ababababyi","ababababyj","ababababyk","ababababyl","ababababym","ababababyn","ababababyo","ababababyp","ababababyq","ababababyr","ababababys","ababababyt","ababababyu","ababababyv","ababababyw","ababababyx","ababababyy","ababababyz","ababababza","ababababzb","ababababzc","ababababzd","ababababze","ababababzf","ababababzg","ababababzh","ababababzi","ababababzj","ababababzk","ababababzl","ababababzm","ababababzn","ababababzo","ababababzp","ababababzq","ababababzr","ababababzs","ababababzt","ababababzu","ababababzv","ababababzw","ababababzx","ababababzy","ababababzz"]

"""

class Solution:
    def findWords(self, board: List[List[str]], wordDict: List[str]) -> List[str]:

        m = len(board)
        n = len(board[0])

        output = set()
        words11 = {}
        # trie = Trie()
        for _w in wordDict:
            # trie.insert(_w)
            words11[_w] = False

        # wordDict = set(wordDict)

        def find_paths(i, j):
            paths = []

            if j + 1 < n and board[i][j + 1] != '$':
                paths.append((i, j + 1))

            if i + 1 < m and board[i + 1][j] != '$':
                paths.append((i + 1, j))

            if i - 1 >= 0 and board[i - 1][j] != '$':
                paths.append((i - 1, j))

            if j - 1 >= 0 and board[i][j - 1] != '$':
                paths.append((i, j - 1))

            return paths

        def dfs(i, j, k, word):
            status = False
            if board[i][j] == word[k]:
                k += 1
                if k == len(word):
                    return True

                board[i][j] = '$'
                paths = find_paths(i, j)
                for path in paths:
                    if dfs(path[0], path[1], k, word):
                        status = True
                        break
                board[i][j] = word[k - 1]

            return status

        for word in wordDict:
            for i in range(0, len(board)):
                if words11[word] == True:
                    break
                for j in range(0, len(board[0])):
                    print(word, i, j)
                    if dfs(i, j, 0, word):
                        output.add(word)
                        words11[word] = True

        return list(output)

"""
TLE below code also
"""


class Solution:
    def findWords(self, board: List[List[str]], wordDict: List[str]) -> List[str]:

        m = len(board)
        n = len(board[0])

        output = set()
        starting = defaultdict(list)
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                starting[board[i][j]].append((i, j))
        print(dict(starting))

        # trie = Trie()
        # trie.insert(_w)

        # wordDict = set(wordDict)

        def find_paths(i, j, k, word):
            paths = []
            p = word[k]

            if j + 1 < n and board[i][j + 1] == p:
                paths.append((i, j + 1))

            if i + 1 < m and board[i + 1][j] == p:
                paths.append((i + 1, j))

            if i - 1 >= 0 and board[i - 1][j] == p:
                paths.append((i - 1, j))

            if j - 1 >= 0 and board[i][j - 1] == p:
                paths.append((i, j - 1))

            return paths

        def dfs(i, j, k, word):
            if k == len(word):
                return True

            status = False
            temp = board[i][j]
            board[i][j] = '$'
            paths = find_paths(i, j, k, word)
            for path in paths:
                if dfs(path[0], path[1], k + 1, word):
                    status = True
                    break
            board[i][j] = temp

            return status

        for word in wordDict:
            startings = starting[word[0]]
            for starts in startings:
                print(word, starts)
                if dfs(starts[0], starts[1], 1, word):
                    output.add(word)

        return list(output)

