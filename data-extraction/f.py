props = [
    'http://www.wikidata.org/prop/direct/described by source',
    'http://schema.org/version',
    'http://www.wikidata.org/prop/direct/Microsoft Academic ID',
    'http://www.wikidata.org/prop/direct/Quora topic ID',
    'http://www.wikidata.org/prop/direct/designed by',
    'http://www.wikidata.org/prop/direct/influenced by',
    'http://www.wikidata.org/prop/direct/programming paradigm',
    'http://www.wikidata.org/prop/direct/file extension',
    'http://www.wikidata.org/prop/direct/named after',
    'http://www.wikidata.org/prop/direct/GitHub topic',
    'http://www.wikidata.org/prop/direct/Google Knowledge Graph ID',
    'http://www.wikidata.org/prop/direct/MIME type',
    'http://www.wikidata.org/prop/direct/instance of',
    'http://www.wikidata.org/prop/direct/Stack Exchange tag',
    'http://www.wikidata.org/prop/direct/developer',
    'http://www.w3.org/2000/01/rdf-schema#label',
    'http://www.wikidata.org/prop/direct/typing discipline',
    'http://www.wikidata.org/prop/direct/inception',
    'http://www.wikidata.org/prop/direct/Freebase ID',
    'http://www.wikidata.org/prop/direct/dialect of computer language',
    'http://www.wikidata.org/prop/direct/subreddit',
    'http://www.wikidata.org/prop/direct/icon',
    'http://www.wikidata.org/prop/direct/discoverer or inventor',
    'http://www.wikidata.org/prop/direct/official website',
    'http://www.wikidata.org/prop/direct/country',
    'http://www.w3.org/2004/02/skos/core#altLabel',
    'http://www.wikidata.org/prop/direct/image'
]

from pyfuseki import FusekiUpdate
from rdflib import Graph, Namespace

from src.logger import LOGGER


def insert(sparql_query):
    g = Graph()
    ela = Namespace("http://www.semanticweb.org/ontologies/ELA#")
    g.update(sparql_query)
    fuseki = FusekiUpdate('http://localhost:3030', 'ELA')
    try:
        fuseki.insert_graph(g)
    except Exception as e:
        LOGGER.error(str(e))


q = """
PREFIX re: <http://www.w3.org/2000/10/swap/reason#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
INSERT DATA {
 ela:Q244627 rdf:type ela:esolang ;
 ela:developer ela:Urban_Müller ;
 ela:programming_paradigm ela:esoteric_programming ;
 ela:programming_paradigm ela:imperative_programming ;
 ela:influenced_by ela:FALSE ;
 ela:influenced_by ela:P-prime-prime .
 ela:Q244627
 ela:version "2035099564"^^xsd:string ;
 ela:Microsoft_Academic_ID "2779854571"^^xsd:string ;
 ela:Quora_topic_ID "Brainfuck-programming-language"^^xsd:string ;
 ela:Stack_Exchange_tag "https://stackoverflow.com/tags/brainfuck"^^xsd:string ;
 ela:creation "1993-01-01T00:00:00Z"^^xsd:date ;
 ela:Freebase_ID "/m/01b5k"^^xsd:string ;
 ela:file_extension "bf"^^xsd:string ;
 ela:file_extension "b"^^xsd:string ;
 ela:icon "http://commons.wikimedia.org/wiki/Special:FilePath/Brainfuck-mw-logo.png"^^xsd:anyURI ;
 ela:image "http://commons.wikimedia.org/wiki/Special:FilePath/Hello%20World%20Brainfuck.png"^^xsd:anyURI ;
 ela:subreddit "brainfuck"^^xsd:anyURI ;
 rdfs:label "Brainfuck"^^xsd:string ;
 skos:altLabel "Brainf**k"^^xsd:string ;
 skos:altLabel "Брейнфак"^^xsd:string ;
 skos:altLabel "Brainf*ck"^^xsd:string ;
 skos:altLabel "OOk"^^xsd:string ;
 skos:altLabel "Brainfuck"^^xsd:string ;
 skos:altLabel "ภาษาเบรนฟัค"^^xsd:string ;
 skos:altLabel "Брэйнфак"^^xsd:string ;
 skos:altLabel "เบรนฟัก"^^xsd:string ;
 skos:altLabel "Ook!"^^xsd:string ;
 skos:altLabel "b"^^xsd:string ;
 skos:altLabel "Brainf-ck"^^xsd:string ;
 skos:altLabel "Brain Fuck"^^xsd:string ;
 skos:altLabel "BrainFuck"^^xsd:string ;
 skos:altLabel "Heilariðlun"^^xsd:string ;
 skos:altLabel "bf"^^xsd:string ;
 skos:altLabel "BrainF***"^^xsd:string ;
 skos:altLabel "branflakes"^^xsd:string ;
 skos:altLabel "b****fuck"^^xsd:string ;
 skos:altLabel "Brainfsck"^^xsd:string ;
 skos:altLabel "เบรนฟัค"^^xsd:string ;
 skos:altLabel "brainfsck"^^xsd:string ;
 skos:altLabel "brainf**k"^^xsd:string ;
 skos:altLabel "Brainf***"^^xsd:string ;
 skos:altLabel "BF"^^xsd:string ;
 skos:altLabel "Brainfuck Komputillingvo"^^xsd:string .
}
"""
insert(q)

# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
# INSERT DATA {
#  ela:Q244627 rdf:type ela:esolang ;
#  ela:developer ela:Urban_Müller ;
#  ela:programming_paradigm ela:esoteric_programming ;
#  ela:programming_paradigm ela:imperative_programming ;
#  ela:influenced_by ela:FALSE ;
#  ela:influenced_by ela:P-prime-prime .
#  ela:Q244627
#  ela:version "2035099564"^^xsd:string ;
#  ela:Microsoft_Academic_ID "2779854571"^^xsd:string ;
#  ela:Quora_topic_ID "Brainfuck-programming-language"^^xsd:string ;
#  ela:Stack_Exchange_tag "https://stackoverflow.com/tags/brainfuck"^^xsd:string ;
#  ela:creation "1993-01-01T00:00:00Z"^^xsd:date ;
#  ela:Freebase_ID "/m/01b5k"^^xsd:string ;
#  ela:file_extension "bf"^^xsd:string ;
#  ela:file_extension "b"^^xsd:string ;
#  ela:icon "http://commons.wikimedia.org/wiki/Special:FilePath/Brainfuck-mw-logo.png"^^xsd:anyURI ;
#  ela:image "http://commons.wikimedia.org/wiki/Special:FilePath/Hello%20World%20Brainfuck.png"^^xsd:anyURI ;
#  ela:subreddit "brainfuck"^^xsd:anyURI ;
#  rdfs:label "Brainfuck"^^xsd:string ;
#  skos:altLabel "Brainf**k"^^xsd:string ;
#  skos:altLabel "Брейнфак"^^xsd:string ;
#  skos:altLabel "Brainf*ck"^^xsd:string ;
#  skos:altLabel "OOk"^^xsd:string ;
#  skos:altLabel "Brainfuck"^^xsd:string ;
#  skos:altLabel "ภาษาเบรนฟัค"^^xsd:string ;
#  skos:altLabel "Брэйнфак"^^xsd:string ;
#  skos:altLabel "เบรนฟัก"^^xsd:string ;
#  skos:altLabel "Ook!"^^xsd:string ;
#  skos:altLabel "b"^^xsd:string ;
#  skos:altLabel "Brainf-ck"^^xsd:string ;
#  skos:altLabel "Brain Fuck"^^xsd:string ;
#  skos:altLabel "BrainFuck"^^xsd:string ;
#  skos:altLabel "Heilariðlun"^^xsd:string ;
#  skos:altLabel "bf"^^xsd:string ;
#  skos:altLabel "BrainF***"^^xsd:string ;
#  skos:altLabel "branflakes"^^xsd:string ;
#  skos:altLabel "b****fuck"^^xsd:string ;
#  skos:altLabel "Brainfsck"^^xsd:string ;
#  skos:altLabel "เบรนฟัค"^^xsd:string ;
#  skos:altLabel "brainfsck"^^xsd:string ;
#  skos:altLabel "brainf**k"^^xsd:string ;
#  skos:altLabel "Brainf***"^^xsd:string ;
#  skos:altLabel "BF"^^xsd:string ;
#  skos:altLabel "Brainfuck Komputillingvo"^^xsd:string .
# }

# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
# INSERT DATA {
#  ela:Q42478 rdf:type ela:esolang ;
#  ela:developer ela:The_Perl_Foundation ;
#  ela:developer ela:Larry_Wall ;
#  ela:programming_paradigm ela:multi-paradigm_programming ;
#  ela:influenced_by ela:C++ ;
#  ela:influenced_by ela:Unix_shell ;
#  ela:influenced_by ela:Lisp ;
#  ela:influenced_by ela:BASIC ;
#  ela:influenced_by ela:AWK ;
#  ela:influenced_by ela:C ;
#  ela:influenced_by ela:sed ;
#  ela:typing_discipline ela:dynamic_typing .
#  ela:Q42478
#  ela:version "2062142930"^^xsd:string ;
#  ela:Microsoft_Academic_ID "2777002779"^^xsd:string ;
#  ela:Quora_topic_ID "Perl-programming-language-1"^^xsd:string ;
#  ela:Stack_Exchange_tag "https://superuser.com/tags/perl"^^xsd:string ;
#  ela:Stack_Exchange_tag "https://stackoverflow.com/tags/perl"^^xsd:string ;
#  ela:Stack_Exchange_tag "https://ja.stackoverflow.com/tags/perl"^^xsd:string ;
#  ela:creation "1987-01-01T00:00:00Z"^^xsd:date ;
#  ela:Freebase_ID "/m/05zrn"^^xsd:string ;
#  ela:GitHub_topic "perl"^^xsd:string ;
#  ela:image "http://commons.wikimedia.org/wiki/Special:FilePath/Source%20code%20in%20Perl.png"^^xsd:anyURI ;
#  ela:official_website "https://www.perl.org/"^^xsd:anyURI ;
#  ela:subreddit "perl"^^xsd:anyURI ;
#  rdfs:label "Perl"^^xsd:string ;
#  skos:altLabel "Lenguaje de programacion Perl"^^xsd:string ;
#  skos:altLabel "เพิร์ล"^^xsd:string ;
#  skos:altLabel "Patologicznie Eklektyczny Roztrząsacz Śmieci"^^xsd:string ;
#  skos:altLabel "Perl5"^^xsd:string ;
#  skos:altLabel "Perl駱駝"^^xsd:string ;
#  skos:altLabel "Programmeertaal Perl"^^xsd:string ;
#  skos:altLabel "Practical Extraction and Reporting Language"^^xsd:string ;
#  skos:altLabel "Perl/CGI"^^xsd:string ;
#  skos:altLabel "பேர்ள்"^^xsd:string ;
#  skos:altLabel "Perl programming language"^^xsd:string ;
#  skos:altLabel "زبان برنامهنویسی پرل"^^xsd:string ;
#  skos:altLabel "Programmiersprache Perl"^^xsd:string ;
#  skos:altLabel "பெர்ள் நிரலாக்க மொழி"^^xsd:string ;
#  skos:altLabel "Praktika Elprena kaj Resuma Lingvo"^^xsd:string ;
#  skos:altLabel "PEARL语言"^^xsd:string ;
#  skos:altLabel "Програмски језик Перл"^^xsd:string ;
#  skos:altLabel "زبان برنامهٔ نویسی پرل"^^xsd:string ;
#  skos:altLabel "زبان پرل"^^xsd:string ;
#  skos:altLabel "Перл"^^xsd:string ;
#  skos:altLabel "Lenguaje de programación Perl"^^xsd:string ;
#  skos:altLabel "Prel"^^xsd:string ;
#  skos:altLabel "Ngôn ngữ Perl"^^xsd:string ;
#  skos:altLabel "பெர்ள் நிரலாக்கமொழி"^^xsd:string ;
#  skos:altLabel "Datei-Handle"^^xsd:string ;
#  skos:altLabel "perl"^^xsd:string ;
#  skos:altLabel "Lenguaje Perl"^^xsd:string ;
#  skos:altLabel "Perl programozási nyelv"^^xsd:string ;
#  skos:altLabel "Per语言"^^xsd:string ;
#  skos:altLabel "Langage Perl"^^xsd:string ;
#  skos:altLabel "PERL"^^xsd:string ;
#  skos:altLabel "Perl语言"^^xsd:string ;
#  skos:altLabel "펄 프로그래밍 언어"^^xsd:string ;
#  skos:altLabel "કોમ્પ્યુટર નેટવર્ક"^^xsd:string ;
#  skos:altLabel "زبان برنامه نویسی پرل"^^xsd:string ;
#  skos:altLabel "Pearl"^^xsd:string ;
#  skos:altLabel "Perl 5"^^xsd:string ;
#  skos:altLabel "البيرل"^^xsd:string ;
#  skos:altLabel "பேர்ழ்"^^xsd:string ;
#  skos:altLabel "Perl编程语言"^^xsd:string ;
#  skos:altLabel "Practical Extraction and Report Language"^^xsd:string ;
#  skos:altLabel "Tim Toady"^^xsd:string ;
#  skos:altLabel "Perl"^^xsd:string ;
#  skos:altLabel "பேர்ல்"^^xsd:string ;
#  skos:altLabel "פרל"^^xsd:string ;
#  skos:altLabel "實用的提取和報告語言"^^xsd:string ;
#  skos:altLabel "Perl 6"^^xsd:string ;
#  skos:altLabel "Bahasa Practical Extraction and Reporting"^^xsd:string ;
#  skos:altLabel "Pathologically Eclectic Rubbish Lister"^^xsd:string .
# }

# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
# INSERT DATA {
#  ela:Q42478 rdf:type ela:esolang ;
#  ela:developer ela:The_Perl_Foundation ;
#  ela:developer ela:Larry_Wall ;
#  ela:programming_paradigm ela:multi-paradigm_programming ;
#  ela:influenced_by ela:Cpp ;
#  ela:influenced_by ela:Unix_shell ;
#  ela:influenced_by ela:Lisp ;
#  ela:influenced_by ela:BASIC ;
#  ela:influenced_by ela:AWK ;
#  ela:influenced_by ela:C ;
#  ela:influenced_by ela:sed ;
#  ela:typing_discipline ela:dynamic_typing .
#  ela:Q42478
#  ela:version "2062142930"^^xsd:string ;
#  ela:Microsoft_Academic_ID "2777002779"^^xsd:string ;
#  ela:Quora_topic_ID "Perl-programming-language-1"^^xsd:string ;
#  ela:Stack_Exchange_tag "https://superuser.com/tags/perl"^^xsd:string ;
#  ela:Stack_Exchange_tag "https://stackoverflow.com/tags/perl"^^xsd:string ;
#  ela:Stack_Exchange_tag "https://ja.stackoverflow.com/tags/perl"^^xsd:string ;
#  ela:creation "1987-01-01T00:00:00Z"^^xsd:date ;
#  ela:Freebase_ID "/m/05zrn"^^xsd:string ;
#  ela:GitHub_topic "perl"^^xsd:string ;
#  ela:image "http://commons.wikimedia.org/wiki/Special:FilePath/Source%20code%20in%20Perl.png"^^xsd:anyURI ;
#  ela:official_website "https://www.perl.org/"^^xsd:anyURI ;
#  ela:subreddit "perl"^^xsd:anyURI ;
#  rdfs:label "Perl"^^xsd:string ;
#  skos:altLabel "Lenguaje de programacion Perl"^^xsd:string ;
#  skos:altLabel "เพิร์ล"^^xsd:string ;
#  skos:altLabel "Patologicznie Eklektyczny Roztrząsacz Śmieci"^^xsd:string ;
#  skos:altLabel "Perl5"^^xsd:string ;
#  skos:altLabel "Perl駱駝"^^xsd:string ;
#  skos:altLabel "Programmeertaal Perl"^^xsd:string ;
#  skos:altLabel "Practical Extraction and Reporting Language"^^xsd:string ;
#  skos:altLabel "Perl/CGI"^^xsd:string ;
#  skos:altLabel "பேர்ள்"^^xsd:string ;
#  skos:altLabel "Perl programming language"^^xsd:string ;
#  skos:altLabel "زبان برنامهنویسی پرل"^^xsd:string ;
#  skos:altLabel "Programmiersprache Perl"^^xsd:string ;
#  skos:altLabel "பெர்ள் நிரலாக்க மொழி"^^xsd:string ;
#  skos:altLabel "Praktika Elprena kaj Resuma Lingvo"^^xsd:string ;
#  skos:altLabel "PEARL语言"^^xsd:string ;
#  skos:altLabel "Програмски језик Перл"^^xsd:string ;
#  skos:altLabel "زبان برنامهٔ نویسی پرل"^^xsd:string ;
#  skos:altLabel "زبان پرل"^^xsd:string ;
#  skos:altLabel "Перл"^^xsd:string ;
#  skos:altLabel "Lenguaje de programación Perl"^^xsd:string ;
#  skos:altLabel "Prel"^^xsd:string ;
#  skos:altLabel "Ngôn ngữ Perl"^^xsd:string ;
#  skos:altLabel "பெர்ள் நிரலாக்கமொழி"^^xsd:string ;
#  skos:altLabel "Datei-Handle"^^xsd:string ;
#  skos:altLabel "perl"^^xsd:string ;
#  skos:altLabel "Lenguaje Perl"^^xsd:string ;
#  skos:altLabel "Perl programozási nyelv"^^xsd:string ;
#  skos:altLabel "Per语言"^^xsd:string ;
#  skos:altLabel "Langage Perl"^^xsd:string ;
#  skos:altLabel "PERL"^^xsd:string ;
#  skos:altLabel "Perl语言"^^xsd:string ;
#  skos:altLabel "펄 프로그래밍 언어"^^xsd:string ;
#  skos:altLabel "કોમ્પ્યુટર નેટવર્ક"^^xsd:string ;
#  skos:altLabel "زبان برنامه نویسی پرل"^^xsd:string ;
#  skos:altLabel "Pearl"^^xsd:string ;
#  skos:altLabel "Perl 5"^^xsd:string ;
#  skos:altLabel "البيرل"^^xsd:string ;
#  skos:altLabel "பேர்ழ்"^^xsd:string ;
#  skos:altLabel "Perl编程语言"^^xsd:string ;
#  skos:altLabel "Practical Extraction and Report Language"^^xsd:string ;
#  skos:altLabel "Tim Toady"^^xsd:string ;
#  skos:altLabel "Perl"^^xsd:string ;
#  skos:altLabel "பேர்ல்"^^xsd:string ;
#  skos:altLabel "פרל"^^xsd:string ;
#  skos:altLabel "實用的提取和報告語言"^^xsd:string ;
#  skos:altLabel "Perl 6"^^xsd:string ;
#  skos:altLabel "Bahasa Practical Extraction and Reporting"^^xsd:string ;
#  skos:altLabel "Pathologically Eclectic Rubbish Lister"^^xsd:string .
# }

# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX ela: <http://www.semanticweb.org/ontologies/ELA#>
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
# INSERT DATA {
#  ela:Q4053269 rdf:type ela:esolang ;
#  ela:developer ela:Microsoft ;
#  ela:influenced_by ela:Cpp ;
#  ela:influenced_by ela:Java .
#  ela:Q4053269 ela:Google_Knowledge_Graph_ID "/g/1z3t27n3w"^^xsd:string ;
#  ela:version "1729775062"^^xsd:string ;
#
#  rdfs:label "X++"^^xsd:string .
# }
