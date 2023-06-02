from collections import defaultdict


p = 10 ** 9 + 7


class Solution:
    def longestDupSubstring(self, s: str) -> str:

        if len(s) == 0:
            return ""

        roll = [0]*len(s)
        roll[0] = 1

        for k in range(1, len(s)):
            roll[k] = (26*roll[k-1]) % p  # lot of time is saved here

        print(roll)

        def rabin_karp(size):
            hashed = 0
            repeat_str = ""
            _map = defaultdict(list)

            for _p in range(0, size):
                hashed = (hashed * 26 + (ord(s[_p]) - 97)) % p

            _map[hashed].append(0)

            for j in range(size, len(s)):
                # print(size - 1)
                hashed = ((hashed - roll[size - 1] * (ord(s[j - size]) - 97)) % p + p) % p  # +p is to handle negative
                hashed = (hashed * 26 + (ord(s[j]) - 97)) % p

                if hashed in _map:
                    print("match")
                    for start in _map[hashed]:
                        print(s[start: start + size], s[j-size+1: j+1])
                        if s[start: start + size] == s[j-size+1: j+1]:
                            return s[start: start + size]

                else:
                    _map[hashed].append(j-size+1)

            # print(_map)
            return repeat_str


        low = 1
        r = len(s)
        max_repeating_str = ""

        while low <= r:
            mid = low + (r - low)//2

            repeating_str = rabin_karp(mid)
            print(mid, repeating_str)
            if repeating_str:
                max_repeating_str = repeating_str
                low = mid + 1
            else:
                r = mid - 1

        return max_repeating_str


a = Solution().longestDupSubstring("mgaxzfplojddpjfrzilfqyjpzazebfzcosjytdrfvvpepwclvblunqbeuwyybwpepzmjaeptxmzvtexxrjeqwzziayrfnuseqofwzqbseqobtwwnxlplbpmddvqclyrhfjwfkxjlgeigeloldfgmfwopiccldbzbncpbubefbuvknlbpvgzrusrugriafrvifzuewitxhohajtgriyfmdzlvjnoofragmttggkrrhmekzfdfwnhrlclebnamodjjhdivlpwjvsowbrrfkszsrcevpbnsncvkvkvukorxhsjpjqsbyibcjzqcujdxvsjaylpfnlfzyrbwovvejagqhqbwrhjyrwastoacsghlywiavxzwdzjfemesfcxmlmxtjjmumvnynftaerxtbbwcxvyccyfmjvfbjndabsxhuiqinhocnwbuqvuiiuhjhfuprrdfhgaflaptumyqzavtacoplflkrsxsvzzsshsgchmiqckuiwvxfhaaretftavfyxenxjgyfljalysmizvrcqxysimusyjbfrvvugijefhbjnfkqlxmmdioioiqxckongoskkwkgqzygencebqoahoslajgreqbgvusczhifyknmfltbrfzhujvnwirmxalciyqfhuedcqgvmycekgjqillryuzaoateuauitgchfrwojfbfrjdjjevcvdyvtjjbgkeaswldeihxgjzvrffxuukcxkcnkyvobisfjwbdpeesyopqdkocqciphbccswtsknjgltndwhtdgmpvhhbmvivwepbnxcsmslnmfknbmsdwlchbnkbwpgolwlgdoksncacbbfifkbwlibxqjuzymqqetdmlqczzfjvxlrfyzerngcamwqjpkchjytjpjoanxceohtffjzpkhkqkvzadwesogucyxjrihashbrqocckxsmmrzsyffgbztqqcakexrhanzftgungwagwbthpqferfqycuegkmrtvomhsfsezhnlbvggsguhbepopavfsoqvutcgylqwiffwhprepuyaogxmwlndnapijdxzvxonftpxzytyhlbteqzgdkgnchkkihxlvzbabbvdrqlyjdhffyavodrypqbodfhnfrvvhlheaygiqofxmezjlkweujktfsajxhzyqgxuisipahjbldqcfnqtjmcmmmdcdvlrdwnaxvsqghvzcxjtrrijgxytwkmwylymkglwdfixzxsphwjdburekghsyfrrxeruvsmhhbprkjkhvylwetnmtoyiwgpfrayyxmitmrdsekldznhnefugnxithtoowpuzybuqegyynqotzronpmofhenpjluxioajzcksjbmhibulreobznxwtwcuwuntwtbxtpjvqbqmscgbatdvpkhlvcxmsctrayjhvyunftznnrrdubaieyujalsvpjcbvaapahzwmjlilgurathawsrgcrtxqzofeprylrtrrugwkejpwxqekyehmjevswjhlijsdqwsymcftypiqvgwfeecnqqwsfxmlnerpglhwvxqanipwhknvltibibkcocyemrnqhcrfehhghswxlzfskxvyyhkmpofkuutqfvtekzcwjsxvelftqdjkeycbuuckevgbdxbnafanhiryktuamexoyqflbkzvlshgnshfciknksuielaluqmddxjfbkzuhvlizciilkukbedabuymgfhzzgwuufvpgieoxzdgvfbvzwrrktapfijlwpwnxawnjdhwnexljuztezyqzpwhnussuxjpejatdsjdwvopfcbnhlumrspxsrpldvbypvmmrezxcctlpokuqjizgmoyhwuxjibzvtgzmzwttepjbzrhzcvoehqcuyshagupyeiqaxfobcodeanbldnqqabzfrxesjdcwqgrrmwwiqhgvbihtxlhtxaupmutifiqkssmmmzsyfmqenyixorypcqqwogykpdnutdbxkcwmgtuzdxdodfmcsdajwcebvhbifjyahkoeoukkbzxtvokejsdsacmsnwmbldcrovhretafjkbmjgfyatinszlxhanphpmklvvjehgrkuzateqeeboqrmxynzniksciyrsctendetfavwhaxfzetyxcnxfquobhhwkdaqjjtibkqyiiyzkmftjcybrriwximfinrpofdyojqhsphtlbpundbttkivvjwikxclhttmyosptwbuybuesucfmdmpvnauggqqijrhzjxrdobtskctyvlxqebnlrcbntqmotktnzeezdkbpoienebtaqgnuhmkzbmpogippuvuterfkxgokldlzkqliqsgchsxhvzdrqicprdaoytbfetzuqofjyznbkuwwfvniijotnisljyyjhjtumezccnevmdeguupiduvfgbttuomawrciruzuicfkjbmgfgozjzhfqaiovxqzddfdwtucwhmgetcikvsyvxaexzhxfqdoqrogxwurskqrzulkpjjphvldfgthicuptfganovpieincqboorlzzdhjjtskwhpgfjtaoyclvdntygilyhrvybdxerchzgqlwwnvwupulruwediayxgxcorjaqavvpoivmobghzgbzjeqedwivayvcpmfmmehbqrqhcvgnjckksesskvjvbzeiavprknmwylfsmxywxkykhotsujfvimbkxmyaxoysdmhjkpbuzvflkqnnsstskxstjqwisnojdjtqrvxdfrznvyabmcgrwvlelqoynsximbmjynkhzjevkzysthsnxegwmerekeiraxuifchgznixkbiitjfcdsjienxqshuvfyuhoxrglrtaxawrdjhmlzdmrrovytzffgykfksrpeljvzqrvmtfahifqpxbppwpqgrypjhzqamrmbbmbgdsrjlquwukcjdsrigowdnbwvmoigxnoihkcvbscnzlbexxlyyyzkssrwciroteupngylxcwpfwcnpdpgvmreysrqarqoynvegbnhwshqnvewvokndhkfemhqdxgqcqqwxeqeqzwpwicnrgdidzlibcfoujmatlgaqurpmhhifzjjoyrtkublkrompwlkcqvhojwhfoltnyekmptryyqcnifyieeczlgdefqlutqgxpflghzdsxmijrjgdxcblhadtvvpedmnbuwhwhnpkeajjjpyrpzfnpbduxbrhjfhwyvinbjswltxlbtfizkxkwjcoetrwfpqmwkheaiamkhfkgmgxljeogxafcozyvkbyanyzunmrecahlfnkqlkygvpbvlyruzlwzgqjzkzpxddyncodfmyloougiyrphvnaplukrfdxiowgvikyoyxbuymesnrxqvadhifmbguwmrceiloizgrydzgftgwrydjloaofgrrgkiymomzuuwkcedlwtdrdrbsbeunxjgiwcmznzxbgrxfnriehbwjcwbkyjesedutikpfyqarlredjfdvvljgihxcedqoaidaaosnaxvavpkkupqgqjakcsjgmyxotkdlzwputwmqecbzolliozphjrystqtnupyqbvykxyyerckzmrdjdlrfsemwlgejbzjpttlxkeaqtnfnwzngpeywbgvpzawplpmlgstmspvtjiqgbvdvrfbdwufujxxlxgopryjogopbeltokspsjgbcehnlilbmiwyhuaecujkgzmfpzkvicrsfdlhnvqejjeoflnrlzfqgxglulhqypzqrtkkcrrtzzlhzpylsujebfwgqlegekdeqcyxxdtiysaupklipjblbedmfzncuvmlkgmcchngyyvwjzcrmqhzvuabwpmuykuhxeqvnaxpgymdunopitoinbxjfcjdlbooteuczpocgwpdxtqufjxtphqzlsmlyinjumixosqpvlfhmyzqiairxrucddgrbvdccxdizdlsruogbxmzcotumekjjpkcyavitllwyuztzyuylwtotsqmdnfiygxtdokmoczbyfeymtltrbnthqxpomxrotxpnltitsmvkwqkugzqgydtkhfswqxpyhjocibjxxfrundalccpfncasghgyxnwergtreksytwzkkpzvdsrdatxjrkemmgtqfpmngddeucxjjfrtmzlzwljkqyibpjtrepcnssoidrhpuaeezkdjplwxmwvvwvoltwshcrxngjywccbdpeqhhufzeitcesuitnbhlkjrckvqqytluoflaesoorywtmvgyoesjycytvevvgxkgaiulrehgknpmrfqjssmeicajbgjvgvkkxcgxuoixawdqurtjuwxdzrxjlgenronmufxunkpltkgyjayehnuamszwcnnnfnnyqepizroaqzwnahhdjnivcptpqawbintdeinfttyvteitaopricqrnchkvmpvtfyphznbfjawekhctsmshvhnsctszkxyahugosyvleeittuhbrtrarzyavktihhpfnyoviuszfpfffrygaogwkdprdxbgnaopujqlpaxzufnxzjeqagkdlhcrcawskfownetawtpzevwbamawxslswqaexnwvhqajzivvgkfpluseswpoctkpizogahoklwyejhwjhaupeaunvhjpnxxulmbfzbhuxgkvyhdnncjrbmbybotgcvfgwkefjcvehlbbduuumyebdbqwngcydrxrcljhonunlzjaoyadhfughnhaiuqtldknemtksijhkicdlqmynnjhhfioaddsydyrentgymfafichahlorzzflsljiynuqiybusajrrxbldnyemxsukpinwcxiheurlxnyjvzxhdcuoulgjnwmtquymuplfzfgzalonjvgrzehcqycizqdfcgigoztxccoopmdpnnfoxlfrfsqrggacepeufsgwxeziryoelnquygndijphvpwqddjwjamowuubvritqhbahvsoqwskzkhmoxpweiffmitucqyllqrxnviwgexhexakysvkommgxstlglvgydpbzszwlfvecynqieburpxluhbvdycpqlqgegmqsgjwekzresndxensjvrulkxbouzbonpcpofltjedrxzjkdeyxrvbotftfhsjndxbnkjlhqstyhnqxcvrtgukqpqqehuajriegobzdjncfvqodgcxftdqjcjjwtrtptfsmawxaruejrvwesgryrdmycuxcnixlnqnvgbunhjmftagjqxmggrmintwvtgllhufbsebekcfpstzrukekonhynrfnfrhwnifdkwsgvlypcufpcexdvwepxvaqcsupwwihveddagmgietshzryquierxskxnxjuqujcdlthaoemqlqorbpjgekazzrisbjdnyaljchjeuyyqgvyutamrmrgzqqgorggdzdociqgwmryawqdyonrqtzzwosjhymlodrwdhydgwuidhbzl")
# a = Solution().longestDupSubstring("banana")
print(a)

