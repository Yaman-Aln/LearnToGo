import {fetch} from 'wix-fetch';  
import wixData from 'wix-data'; 

export async function ArticleWords_beforeInsert(item, context) {
  item.word = toLower(item.word);
  item.title = item.word.split(' ');
  console.log(item.word);
  item.wordInB2 = ["l'argent", 
  "famille", "histoire", "oncle", "tante", "argent", "naître", "bouche", "épinards", "beurre", "porte-monnaie","soeur","panier","percer","doigt","rapport","accumuler","emprunter","oursin","brûler","paresseuse","radis","cousin","parents","jeter","fenêtre","près","vivre","arbre","poil","l'or","moyens","pousser","empêcher","plage","oublier",
  "juin",
"guerre",
"mondiale",
"commémorer",
"allié",
"souvenir",
"devoir",
"normandie",
"armées",
"navire",
"militaire",
"débarquement",
"côte",
"uniforme",
"soldat",
"parachutiste",
"allemand",
"allemande",
"américain",
"américaine",
"britannique",
"français",
"française",
"vétéran",
"juillet",
"défilé",
"d'artifice",
"férié",
"populaire",
"nationale",
"fête",
"célébrer",
"lampion",
"cocarde",
"bastille",
"république",
"tuyau",
"astuce",
"économiser",
"réduction",
"réduit",
"soldes",
"dépenser",
"acheter",
"affaire",
"inutile",
"spéciale",
"comparer",
"d'occasion",
"achat",
"marché",
"cher",
"frais",
"courses",
"coûter",
"économies",
"côté",
"ouragan",
"pompier",
"urgences",
"tornade",
"évacuation",
"urgentiste",
"secours",
"catastrophe",
"dégâts",
"cyclone",
"inondation",
"secouriste",
"incendie",
"coulée",
"éboulement",
"détruire",
"s'écrouler",
"tempête",
"terrifiant",
"destructeur",
"d'électricité",
"raz-de-marée",
"journaliste",
"pigiste",
"chroniqueur",
"chroniqueuse",
"sujet",
"colonne",
"article",
"critique",
"interview",
"entretien",
"exclusif",
"exclusive",
"interviewer",
"invité",
"invitée",
"source",
"fiable",
"impartial",
"coquille",
"légende",
"délais",
"camping",
"camper",
"camping",
"tente",
"tente",
"s'installer",
"étoile",
"couchage",
"camp",
"dos",
"poche",
"ouvre-boîte",
"randonnée",
"dessinée",
"lire",
"auteur",
"graphiste",
"illustrateur",
"illustratrice",
"dessinateur",
"dessinatrice",
"encreur",
"encreuse",
"dialogue",
"personnage",
"intrigue",
"planche",
"bulle",
"vignette",
"onomatopée",
"neuf",
"aider",
"apprendre",
"arriver",
"avoir",
"chercher",
"commencer",
"consentir",
"encourager",
"enseigner",
"hésiter",
"inviter",
"obliger",
"s’amuser",
"s’apprêter",
"s’attendre",
"s’habituer",
"se préparer",
"perdre",
"occasion",
"vue",
"latin"];

  
  item.foundB2='';
  console.log(item.title)

// Runs a query on the "recipes" collection
    let matchWord = ''
for (let y = 0; y < item.title.length; y++) {
    await wixData.query("ArticleWords") 
  // Query the collection for any items whose "Name" field contains  
  // the value the user entered in the input element
    .eq("wordInB2", item.title[y])
  .find()  // Run the query
  .then(res => {  
    if (res.totalCount>0) {
        matchWord = matchWord +'\n'+ item.title[y]
    }
  }
  )
.then( res =>{  
item.foundB2 = matchWord
}
)
}
return item;  
}

function toLower(s) {
  return s.charAt(0).toLowerCase() + s.slice(1);
}
