from random import choice

animal_names = [
  "Aardwolf",
  "Acanthaster planci",
  "Admiral",
  "African black crake",
  "African buffalo",
  "African bush squirrel",
  "African clawless otter",
  "African darter",
  "African elephant",
  "African fish eagle",
  "African jacana",
  "African lion",
  "African lynx",
  "African pied wagtail",
  "African polecat",
  "African porcupine",
  "African skink",
  "African wild cat",
  "African wild dog",
  "Agile wallaby",
  "Agouti",
  "Agouti paca",
  "Albatross",
  "Alcelaphus buselaphus caama",
  "Alcelaphus buselaphus cokii",
  "Alces alces",
  "Alectura lathami",
  "Alligator",
  "Alpaca",
  "American alligator",
  "American badger",
  "American beaver",
  "American bighorn sheep",
  "American bison",
  "American black bear",
  "American buffalo",
  "American crow",
  "American marten",
  "American racer",
  "American Virginia opossum",
  "American woodcock",
  "Ammospermophilus nelsoni",
  "Anas platyrhynchos",
  "Anas punctata",
  "Anastomus oscitans",
  "Anathana ellioti",
  "Andean goose",
  "Anhinga rufa",
  "Anser anser",
  "Anser caerulescens",
  "Anteater",
  "Antechinus",
  "Antechinus flavipes",
  "Antelope",
  "Antelope ground squirrel",
  "Anthropoides paradisea",
  "Antilocapra americana",
  "Antilope cervicapra",
  "Aonyx cinerea",
  "Aquila chrysaetos",
  "Ara ararauna",
  "Ara chloroptera",
  "Ara macao",
  "Arboral spiny rat",
  "Arctic fox",
  "Arctic ground squirrel",
  "Arctic hare",
  "Arctic lemming",
  "Arctic tern",
  "Arctogalidia trivirgata",
  "Ardea cinerea",
  "Ardea golieth",
  "Argalis",
  "Armadillo",
  "Asian elephant",
  "Asian false vampire bat",
  "Asian foreset tortoise",
  "Asian lion",
  "Asian openbill",
  "Asian red fox",
  "Asian water buffalo",
  "Asian water dragon",
  "Asiatic jackal",
  "Asiatic wild ass",
  "Ass",
  "Australian brush turkey",
  "Australian magpie",
  "Australian masked owl",
  "Australian pelican",
  "Australian sea lion",
  "Australian spiny anteater",
  "Avocet",
  "Azara's zorro",
  "Baboon",
  "Badger",
  "Bahama pintail",
  "Bald eagle",
  "Balearica pavonina",
  "Baleen whale",
  "Banded mongoose",
  "Bandicoot",
  "Barasingha deer",
  "Barbet",
  "Barking gecko",
  "Barrows goldeneye",
  "Bat",
  "Bateleur eagle",
  "Bear",
  "Beaver",
  "Beisa oryx",
  "Bengal vulture",
  "Bennett's wallaby",
  "Bettong",
  "Bettongia penicillata",
  "Bird",
  "Bison",
  "Bison bison",
  "Black bear",
  "Blackbird",
  "Blackbuck",
  "Black curlew",
  "Blackish oystercatcher",
  "Black kite",
  "Black rhinoceros",
  "Blacksmith plover",
  "Black spider monkey",
  "Black swan",
  "Black vulture",
  "Bleeding heart monkey",
  "Blesbok",
  "Bleu",
  "Blue and gold macaw",
  "Blue and yellow macaw",
  "Blue catfish",
  "Blue crane",
  "Blue duck",
  "Blue fox",
  "Blue peacock",
  "Blue racer",
  "Blue shark",
  "Blue waxbill",
  "Blue wildebeest",
  "Boa",
  "Boa constrictor mexicana",
  "Boar",
  "Bobcat",
  "Bohor reedbuck",
  "Bonnet macaque",
  "Bontebok",
  "Booby",
  "Boubou",
  "Brazilian otter",
  "Brazilian tapir",
  "Brindled gnu",
  "Brocket",
  "Brolga crane",
  "Brown and yellow marshbird",
  "Brown brocket",
  "Brown capuchin",
  "Brown hyena",
  "Brown lemur",
  "Brown pelican",
  "Btop",
  "Bubalornis niger",
  "Bubalus arnee",
  "Bucephala clangula",
  "Bucorvus leadbeateri",
  "Buffalo",
  "Bulbul",
  "Bunting",
  "Burchell's gonolek",
  "Burmese black mountain tortoise",
  "Burmese brown mountain tortoise",
  "Burrowing owl",
  "Bushbaby",
  "Bushbuck",
  "Bush dog",
  "Bushpig",
  "Bustard",
  "Butterfly",
  "Buttermilk snake",
  "Cacatua galerita",
  "Caiman",
  "California sea lion",
  "Callipepla gambelii",
  "Camel",
  "Campo flicker",
  "Canada goose",
  "Canadian river otter",
  "Canadian tiger swallowtail butterfly",
  "Canis dingo",
  "Canis latrans",
  "Canis lupus baileyi",
  "Canis lupus lycaon",
  "Canis mesomelas",
  "Cape Barren goose",
  "Cape clawless otter",
  "Cape cobra",
  "Cape fox",
  "Cape raven",
  "Cape starling",
  "Cape wild cat",
  "Capra ibex",
  "Capuchin",
  "Capybara",
  "Caracal",
  "Caracara",
  "Cardinal",
  "Caribou",
  "Carpet python",
  "Carpet snake",
  "Castor fiber",
  "Cat",
  "Catfish",
  "Catharacta skua",
  "Cathartes aura",
  "Cattle egret",
  "Cebus albifrons",
  "Cebus apella",
  "Ceratotherium simum",
  "Cercopithecus aethiops",
  "Cereopsis goose",
  "Cereopsis novaehollandiae",
  "Certotrichas paena",
  "Cervus duvauceli",
  "Cervus unicolor",
  "Chacma baboon",
  "Chauna torquata",
  "Cheetah",
  "Chestnut weaver",
  "Chickadee",
  "Chilean flamingo",
  "Chimpanzee",
  "Chionis alba",
  "Chipmunk",
  "Chital",
  "Chlamydosaurus kingii",
  "Chloephaga melanoptera",
  "Choloepus hoffmani",
  "Chordeiles minor",
  "Choriotis kori",
  "Chuckwalla",
  "Ciconia ciconia",
  "Civet",
  "Civet cat",
  "Clark's nutcracker",
  "Cliffchat",
  "Climacteris melanura",
  "Coatimundi",
  "Cobra",
  "Cockatoo",
  "Coke's hartebeest",
  "Colaptes campestroides",
  "Collared lemming",
  "Collared lizard",
  "Collared peccary",
  "Colobus",
  "Colobus guerza",
  "Coluber constrictor",
  "Coluber constrictor foxii",
  "Columba livia",
  "Columbian rainbow boa",
  "Comb duck",
  "Common boubou shrike",
  "Common brushtail possum",
  "Common dolphin",
  "Common duiker",
  "Common eland",
  "Common genet",
  "Common goldeneye",
  "Common green iguana",
  "Common grenadier",
  "Common langur",
  "Common melba finch",
  "Common mynah",
  "Common nighthawk",
  "Common palm civet",
  "Common pheasant",
  "Common raccoon",
  "Common rhea",
  "Common ringtail",
  "Common seal",
  "Common shelduck",
  "Common turkey",
  "Common wallaroo",
  "Common waterbuck",
  "Common wolf",
  "Common wombat",
  "Common zebra",
  "Common zorro",
  "Constrictor",
  "Cook's tree boa",
  "Coot",
  "Coqui francolin",
  "Coqui partridge",
  "Coracias caudata",
  "Corallus hortulanus cooki",
  "Corella",
  "Cormorant",
  "Corvus brachyrhynchos",
  "Corythornis cristata",
  "Cottonmouth",
  "Cougar",
  "Cow",
  "Coyote",
  "Crab",
  "Crake",
  "Crane",
  "Creeper",
  "Crested barbet",
  "Crested bunting",
  "Crested porcupine",
  "Crested screamer",
  "Crocodile",
  "Crocuta crocuta",
  "Crotalus cerastes",
  "Crow",
  "Crowned eagle",
  "Crown of thorns starfish",
  "Ctop",
  "Cuis",
  "Curlew",
  "Cygnus buccinator",
  "Cynictis penicillata",
  "Dabchick",
  "Dacelo novaeguineae",
  "Damaliscus dorcas",
  "Dama wallaby",
  "Darter",
  "Dassie",
  "Dasyprocta leporina",
  "Deer",
  "Defassa waterbuck",
  "Dendrocitta vagabunda",
  "Dendrocygna viduata",
  "Dendrohyrax brucel",
  "Denham's bustard",
  "Desert kangaroo rat",
  "Desert spiny lizard",
  "Desert tortoise",
  "Devil",
  "Didelphis virginiana",
  "Dik",
  "Dingo",
  "Diomedea irrorata",
  "Dipodomys deserti",
  "Dog",
  "Dolichitus patagonum",
  "Dolphin",
  "Dove",
  "Downy woodpecker",
  "Dragon",
  "Dragonfly",
  "Dromaeus novaehollandiae",
  "Dromedary camel",
  "Drongo",
  "Drymarchon corias couperi",
  "Dtop",
  "Duck",
  "Duiker",
  "Dunnart",
  "Dusky gull",
  "Dusky rattlesnake",
  "Eagle",
  "Echidna",
  "Egret",
  "Egretta thula",
  "Egyptian cobra",
  "Egyptian goose",
  "Egyptian viper",
  "Egyptian vulture",
  "Eira barbata",
  "Eland",
  "Elegant crested tinamou",
  "Elephant",
  "Elk",
  "Emerald green tree boa",
  "Emu",
  "Ephippiorhynchus mycteria",
  "Equus burchelli",
  "Erethizon dorsatum",
  "Estrilda erythronotos",
  "Etop",
  "Eudromia elegans",
  "Eudyptula minor",
  "Eurasian badger",
  "Eurasian beaver",
  "Eurasian hoopoe",
  "Eurasian red squirrel",
  "Eurocephalus anguitimens",
  "European badger",
  "European beaver",
  "European red squirrel",
  "European shelduck",
  "European spoonbill",
  "European stork",
  "European wild cat",
  "Euro wallaby",
  "Fairy penguin",
  "Falcon",
  "Feathertail glider",
  "Felis caracal",
  "Felis concolor",
  "Felis libyca",
  "Felis serval",
  "Felis silvestris lybica",
  "Felis wiedi or Leopardus weidi",
  "Felis yagouaroundi",
  "Feral rock pigeon",
  "Ferret",
  "Ferruginous hawk",
  "Field flicker",
  "Finch",
  "Fisher",
  "Flamingo",
  "Flicker",
  "Flightless cormorant",
  "Flycatcher",
  "Fowl",
  "Fox",
  "Francolin",
  "Francolinus coqui",
  "Francolinus swainsonii",
  "Fratercula corniculata",
  "Fregata magnificans",
  "Frilled dragon",
  "Frilled lizard",
  "Frogmouth",
  "Ftop",
  "Fulica cristata",
  "Funambulus pennati",
  "Galah",
  "Galapagos albatross",
  "Galapagos dove",
  "Galapagos hawk",
  "Galapagos mockingbird",
  "Galapagos penguin",
  "Galapagos sea lion",
  "Galapagos tortoise",
  "Galictis vittata",
  "Gambel's quail",
  "Gaur",
  "Gazella granti",
  "Gazella thompsonii",
  "Gazelle",
  "Gazer",
  "Gecko",
  "Gekko gecko",
  "Gelada baboon",
  "Gemsbok",
  "Genet",
  "Genetta genetta",
  "Genoveva",
  "Geochelone elegans",
  "Geochelone radiata",
  "Gerenuk",
  "Giant anteater",
  "Giant armadillo",
  "Giant girdled lizard",
  "Giant heron",
  "Giant otter",
  "Gila monster",
  "Giraffe",
  "Glider",
  "Globicephala melas",
  "Gnu",
  "Goanna lizard",
  "Goat",
  "Godwit",
  "Golden eagle",
  "Goldeneye",
  "Golden jackal",
  "Goliath heron",
  "Gonolek",
  "Goose",
  "Gopherus agassizii",
  "Gorilla",
  "Gorilla gorilla",
  "Grant's gazelle",
  "Gray duiker",
  "Gray heron",
  "Gray langur",
  "Gray rhea",
  "Great cormorant",
  "Great egret",
  "Greater adjutant stork",
  "Greater flamingo",
  "Greater kudu",
  "Greater rhea",
  "Greater roadrunner",
  "Greater sage grouse",
  "Great horned owl",
  "Great kiskadee",
  "Great skua",
  "Great white pelican",
  "Grebe",
  "Green heron",
  "Green vine snake",
  "Grenadier",
  "Grey fox",
  "Grey heron",
  "Greylag goose",
  "Grey lourie",
  "Grey mouse lemur",
  "Grey phalarope",
  "Griffon vulture",
  "Grison",
  "Grizzly bear",
  "Groundhog",
  "Ground legaan",
  "Grouse",
  "Grus antigone",
  "Gtop",
  "Guanaco",
  "Guerza",
  "Gull",
  "Gymnorhina tibicen",
  "Haematopus ater",
  "Haliaetus leucogaster",
  "Haliaetus vocifer",
  "Hanuman langur",
  "Harbor seal",
  "Hare",
  "Hartebeest",
  "Hawk",
  "Hedgehog",
  "Helmeted guinea fowl",
  "Heloderma horridum",
  "Helogale undulata",
  "Hen",
  "Heron",
  "Herring gull",
  "Hippopotamus",
  "Hippotragus niger",
  "Hoary marmot",
  "Hoffman's sloth",
  "Honey badger",
  "Hoopoe",
  "Hornbill",
  "Horned lark",
  "Horned puffin",
  "Horned rattlesnake",
  "Hottentot teal",
  "House crow",
  "House sparrow",
  "Htop",
  "Hudsonian godwit",
  "Huron",
  "Hyaena brunnea",
  "Hyaena hyaena",
  "Hyena",
  "Hyrax",
  "Hystrix cristata",
  "Hystrix indica",
  "Ibex",
  "Ibis",
  "Iguana",
  "Iguana iguana",
  "Impala",
  "Indian giant squirrel",
  "Indian jackal",
  "Indian leopard",
  "Indian mynah",
  "Indian peacock",
  "Indian porcupine",
  "Indian red admiral",
  "Indian star tortoise",
  "Indian tree pie",
  "Insect",
  "Itop",
  "Jabiru stork",
  "Jacana",
  "Jackal",
  "Jackrabbit",
  "Jaeger",
  "Jaguar",
  "Jaguarundi",
  "Japanese macaque",
  "Javanese cormorant",
  "Jtop",
  "Jungle cat",
  "Jungle kangaroo",
  "Junonia genoveua",
  "Kaffir cat",
  "Kafue flats lechwe",
  "Kalahari scrub robin",
  "Kangaroo",
  "Kelp gull",
  "Killer whale",
  "King cormorant",
  "Kingfisher",
  "King vulture",
  "Kinkajou",
  "Kirk's dik dik",
  "Kiskadee",
  "Kite",
  "Klipspringer",
  "Koala",
  "Kobus defassa",
  "Kobus leche robertsi",
  "Kobus vardonii vardoni",
  "Komodo dragon",
  "Kongoni",
  "Kookaburra",
  "Kori bustard",
  "Ktop",
  "Kudu",
  "Lama glama",
  "Lama guanicoe",
  "Lama pacos",
  "Lamprotornis nitens",
  "Land iguana",
  "Langur",
  "Lapwing",
  "Large cormorant",
  "Lark",
  "Larus novaehollandiae",
  "Lasiodora parahybana",
  "Lasiorhinus latifrons",
  "Laughing dove",
  "Laughing kookaburra",
  "Lava gull",
  "Leadbeateri's ground hornbill",
  "Least chipmunk",
  "Lechwe",
  "Legaan",
  "Leipoa ocellata",
  "Lemming",
  "Lemur",
  "Lemur catta",
  "Leopard",
  "Lepilemur rufescens",
  "Leprocaulinus vipera",
  "Lepus townsendii",
  "Lesser flamingo",
  "Lesser masked weaver",
  "Lesser mouse lemur",
  "Levaillant's barbet",
  "Libellula quadrimaculata",
  "Lily trotter",
  "Limnocorax flavirostra",
  "Limosa haemastica",
  "Lion",
  "Litrocranius walleri",
  "Little blue penguin",
  "Little brown bat",
  "Little brown dove",
  "Little cormorant",
  "Little grebe",
  "Little heron",
  "Lizard",
  "Llama",
  "Lorikeet",
  "Loris",
  "Lory",
  "Lorythaixoides concolor",
  "Lourie",
  "Loxodonta africana",
  "Ltop",
  "Lycosa godeffroyi",
  "Lynx",
  "Mabuya spilogaster",
  "Macaca fuscata",
  "Macaca mulatta",
  "Macaca nemestrina",
  "Macaca radiata",
  "Macaque",
  "Macaw",
  "Macropus eugenii",
  "Macropus parryi",
  "Madagascar fruit bat",
  "Madagascar hawk owl",
  "Madoqua kirkii",
  "Magellanic penguin",
  "Magnificent frigate bird",
  "Magpie",
  "Malabar squirrel",
  "Malachite kingfisher",
  "Malagasy ground boa",
  "Mallard",
  "Malleefowl",
  "Manatee",
  "Mandras tree shrew",
  "Manouria emys",
  "Mara",
  "Marabou stork",
  "Margay",
  "Marine iguana",
  "Marmot",
  "Marmota caligata",
  "Marmota monax",
  "Marshbird",
  "Marten",
  "Martes americana",
  "Martes pennanti",
  "Masked booby",
  "Mazama americana",
  "Mazama gouazoubira",
  "Meerkat",
  "Megaderma spasma",
  "Meleagris gallopavo",
  "Meles meles",
  "Melophus lathami",
  "Merops bullockoides",
  "Mexican beaded lizard",
  "Mexican boa",
  "Mexican wolf",
  "Milvago chimachima",
  "Milvus migrans",
  "Miner's cat",
  "Mirounga leonina",
  "Mississippi alligator",
  "Moccasin",
  "Mockingbird",
  "Mocking cliffchat",
  "Mongoose",
  "Monitor",
  "Monkey",
  "Monster",
  "Moorhen",
  "Moose",
  "Morelia spilotes variegata",
  "Motacilla aguimp",
  "Mouflon",
  "Mountain duck",
  "Mountain goat",
  "Mountain lion",
  "Mourning collared dove",
  "Mouse",
  "Mtop",
  "Mule deer",
  "Mungos mungo",
  "Musk ox",
  "Mustela nigripes",
  "Mycteria leucocephala",
  "Myiarchus tuberculifer",
  "Mynah",
  "Myrmecophaga tridactyla",
  "Naja haje",
  "Naja nivea",
  "Nannopterum harrisi",
  "Nasua narica",
  "Nasua nasua",
  "Native cat",
  "Nectarinia chalybea",
  "Nelson ground squirrel",
  "Neophoca cinerea",
  "Neotis denhami",
  "Neotropic cormorant",
  "Netted rock dragon",
  "Nighthawk",
  "Nile crocodile",
  "Nilgai",
  "North American beaver",
  "North American porcupine",
  "North American red fox",
  "North American river otter",
  "Ntop",
  "Nucifraga columbiana",
  "Numbat",
  "Nutcracker",
  "Nuthatch",
  "Nyala",
  "Nyctanassa violacea",
  "Nyctea scandiaca",
  "Nyctereutes procyonoides",
  "Nycticorax nycticorax",
  "Ocelot",
  "Olive baboon",
  "Onager",
  "Oncorhynchus nerka",
  "Openbill",
  "Openbill stork",
  "Opossum",
  "Orca",
  "Orcinus orca",
  "Oribi",
  "Ornate rock dragon",
  "Oryx",
  "Oryx gazella",
  "Osprey",
  "Ostrich",
  "Otaria flavescens",
  "Otop",
  "Otter",
  "Ourebia ourebi",
  "Ovenbird",
  "Ovis ammon",
  "Ovis dalli stonei",
  "Ovis musimon",
  "Owl",
  "Ox",
  "Oystercatcher",
  "Paca",
  "Pacific gull",
  "Pademelon",
  "Painted stork",
  "Pallas's fish eagle",
  "Palm squirrel",
  "Pampa gray fox",
  "Panthera leo",
  "Panthera leo persica",
  "Panthera onca",
  "Pan troglodytes",
  "Paradoxure",
  "Parakeet",
  "Paraxerus cepapi",
  "Parrot",
  "Partridge",
  "Peacock",
  "Peccary",
  "Pelican",
  "Penguin",
  "Perameles nasuta",
  "Peregrine falcon",
  "Petaurus breviceps",
  "Phalacrocorax albiventer",
  "Phalacrocorax carbo",
  "Phalacrocorax niger",
  "Phalarope",
  "Phascogale",
  "Phascogale calura",
  "Phascogale tapoatafa",
  "Pheasant",
  "Phoca vitulina",
  "Phoeniconaias minor",
  "Phoenicopterus ruber",
  "Phylurus milli",
  "Picoides pubescens",
  "Pie",
  "Pied avocet",
  "Pied butcher bird",
  "Pied cormorant",
  "Pied crow",
  "Pied kingfisher",
  "Pigeon",
  "Pine siskin",
  "Pine squirrel",
  "Pintail",
  "Plains zebra",
  "Platalea leucordia",
  "Platypus",
  "Plegadis ridgwayi",
  "Plocepasser mahali",
  "Plover",
  "Podargus strigoides",
  "Polar bear",
  "Polecat",
  "Porcupine",
  "Porphyrio porphyrio",
  "Possum",
  "Potoroo",
  "Prairie falcon",
  "Prionace glauca",
  "Procyon lotor",
  "Pronghorn",
  "Propithecus verreauxi",
  "Pseudoleistes virescens",
  "Psittacula krameri",
  "Ptop",
  "Puffin",
  "Puku",
  "Puma",
  "Purple grenadier",
  "Purple moorhen",
  "Pycnonotus nigricans",
  "Pygmy possum",
  "Python",
  "Pytilia melba",
  "Qtop",
  "Quail",
  "Quoll",
  "Rabbit",
  "Raccoon",
  "Raccoon dog",
  "Racer",
  "Racer snake",
  "Radiated tortoise",
  "Rainbow lory",
  "Rat",
  "Rattlesnake",
  "Ratufa indica",
  "Raven",
  "Recurvirostra avosetta",
  "Red and blue macaw",
  "Red brocket",
  "Red deer",
  "Red hartebeest",
  "Red howler monkey",
  "Red kangaroo",
  "Red lava crab",
  "Red meerkat",
  "Red phalarope",
  "Red sheep",
  "Red squirrel",
  "Redunca redunca",
  "Reedbuck",
  "Reindeer",
  "Rhabdomys pumilio",
  "Rhea",
  "Rhea americana",
  "Rhesus macaque",
  "Rhesus monkey",
  "Rhinoceros",
  "Richardson's ground squirrel",
  "Ring dove",
  "Ringtail",
  "Ringtail cat",
  "River wallaby",
  "Roadrunner",
  "Roan antelope",
  "Robin",
  "Rock dove",
  "Roe deer",
  "Roller",
  "Roseate cockatoo",
  "Roseat flamingo",
  "Royal tern",
  "Rtop",
  "Rufous tree pie",
  "Russian dragonfly",
  "Sable antelope",
  "Sage grouse",
  "Sage hen",
  "Sally lightfoot crab",
  "Salmon",
  "Salmon pink bird eater tarantula",
  "Sambar",
  "Sandgrouse",
  "Sandhill crane",
  "Sandpiper",
  "Sarcophilus harrisii",
  "Sarcorhamphus papa",
  "Sarkidornis melanotos",
  "Sarus crane",
  "Savanna baboon",
  "Savanna fox",
  "Savannah deer",
  "Scarlet macaw",
  "Sceloporus magister",
  "Sciurus niger",
  "Scolopax minor",
  "Scottish highland cow",
  "Screamer",
  "Seal",
  "Secretary bird",
  "Serval",
  "Shark",
  "Sheathbill",
  "Sheep",
  "Shelduck",
  "Shrew",
  "Shrike",
  "Sidewinder",
  "Sifaka",
  "Silver gull",
  "Siskin",
  "Skimmer",
  "Skink",
  "Skua",
  "Skunk",
  "Sloth",
  "Sloth bear",
  "Small Indian mongoose",
  "Smithopsis crassicaudata",
  "Smith's bush squirrel",
  "Snake",
  "Snow goose",
  "Snowy egret",
  "Snowy owl",
  "Snowy sheathbill",
  "Snycerus caffer",
  "Sociable weaver",
  "Sockeye salmon",
  "South African hedgehog",
  "South American puma",
  "South American sea lion",
  "Sparrow",
  "Spectacled caiman",
  "Speotyte cuniculata",
  "Spermophilus parryii",
  "Spermophilus richardsonii",
  "Spider",
  "Spoonbill",
  "Sportive lemur",
  "Spotted deer",
  "Spotted hyena",
  "Spotted wood sandpiper",
  "Springbok",
  "Springbuck",
  "Springhare",
  "Spurfowl",
  "Squirrel",
  "Squirrel glider",
  "Stanley bustard",
  "Stanley crane",
  "Starfish",
  "Starling",
  "Steenbok",
  "Steenbuck",
  "Steller sea lion",
  "Steller's sea lion",
  "Stenella coeruleoalba",
  "Sterna paradisaea",
  "Stick insect",
  "Stilt",
  "Stone sheep",
  "Stop",
  "Stork",
  "Streptopelia decipiens",
  "Striated heron",
  "Striped dolphin",
  "Striped hyena",
  "Striped skunk",
  "Sugar glider",
  "Sula dactylatra",
  "Sula nebouxii",
  "Sunbird",
  "Sun gazer",
  "Sungazer",
  "Superb starling",
  "Suricata suricatta",
  "Suricate",
  "Sus scrofa",
  "Swainson's francolin",
  "Swamp deer",
  "Swan",
  "Sylvicapra grimma",
  "Tadorna tadorna",
  "Tailless tenrec",
  "Tamandua",
  "Tamandua tetradactyla",
  "Tammar wallaby",
  "Tapir",
  "Tarantula",
  "Tasmanian devil",
  "Taurotagus oryx",
  "Tawny eagle",
  "Tawny frogmouth",
  "Tayassu pecari",
  "Tayassu tajacu",
  "Tayra",
  "Teal",
  "Tenrec",
  "Tern",
  "Terrapene carolina",
  "Theropithecus gelada",
  "Thomson's gazelle",
  "Thrasher",
  "Thylogale stigmatica",
  "Tiger",
  "Tiger cat",
  "Tiger snake",
  "Tiliqua scincoides",
  "Timber wolf",
  "Tinamou",
  "Toddy cat",
  "Tokay gecko",
  "Topi",
  "Tortoise",
  "Toucan",
  "Toxostoma curvirostre",
  "Trachyphonus vaillantii",
  "Tragelaphus angasi",
  "Tragelaphus strepsiceros",
  "Tree porcupine",
  "Trichosurus vulpecula",
  "Tringa glareola",
  "Tropical buckeye butterfly",
  "Trotter",
  "Trumpeter",
  "Trumpeter swan",
  "Tsessebe",
  "Ttop",
  "Turaco",
  "Turkey",
  "Turkey vulture",
  "Turtle",
  "Turtur chalcospilos",
  "Tyrant flycatcher",
  "Tyto novaehollandiae",
  "Uinta ground squirrel",
  "Upupa epops",
  "Uraeginthus granatina",
  "Urial",
  "Ursus arctos",
  "Utop",
  "Vanessa indica",
  "Varanus salvator",
  "Verreaux's sifaka",
  "Vervet monkey",
  "Vicugna vicugna",
  "Vicuna",
  "Viper",
  "Vtop",
  "Vulpes chama",
  "Vulpes vulpes",
  "Vulture",
  "Wagtail",
  "Wallaby",
  "Wallaroo",
  "Wambenger",
  "Wapiti",
  "Warthog",
  "Waterbuck",
  "Water legaan",
  "Water moccasin",
  "Water monitor",
  "Wattled crane",
  "Waved albatross",
  "Waxbill",
  "Weaver",
  "Weeper capuchin",
  "Whale",
  "White rhinoceros",
  "White spoonbill",
  "White stork",
  "Wild boar",
  "Wildebeest",
  "Wild turkey",
  "Wild water buffalo",
  "Wolf",
  "Wolf spider",
  "Wombat",
  "Woodchuck",
  "Woodcock",
  "Woodpecker",
  "Wood pigeon",
  "Woylie",
  "Wtop",
  "Yak",
  "Yellow baboon",
  "Yellow mongoose",
  "Ytop",
  "Zebra",
  "Zenaida asiatica",
  "Zorilla",
  "Zorro",
  "Ztop"
]

def generate_name() -> str:
    return 'unidentified ' + choice(animal_names)