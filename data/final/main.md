---
author:
- Agata SKRZYNIARZ
bibliography: biblio.bib
title: Performance Evaluation of Tools for Automatic Processing of Polish L2 Interlanguage
---

::: center
     
  -------------------------------------- ------------------------------------------
:::

::: center
**Institut National des Langues et Civilisations Orientales**\
(National Institute for Oriental Languages and Civilizations)

Département Textes, Informatique, Multilinguisme\
(Department of Texts, Computing, and Multilingualism)

------------------------------------------------------------------------

**Performance Evaluation of Tools for Automatic Processing of Polish L2 Interlanguage**

------------------------------------------------------------------------

[Master]

[Traitement Automatique des Langues]\
[(Natural Language Processing)]

*Specialization:*

*Research and Development*

by

**Agata [Skrzyniarz]**

*Thesis Supervisor:*

*Sarra El Ayari*

Academic Year 2024/2025
:::

## Abstract 

This thesis investigates the performance of automatic tools in processing Polish interlanguage produced by adult learners from the VILLA project, who completed a route-giving task after 14 hours of instruction. The study has two main objectives: first, to analyze learner deviations in case inflection and pronunciation, revealing patterns such as overuse of the nominative, confusion between genitive, instrumental, and locative forms, and difficulties with retroflex consonants and nasal vowels; second, to evaluate Whisper, an end-to-end ASR system, on its ability to transcribe Polish interlanguage. A detailed analysis shows that Whisper often overcorrects pronunciation errors but reproduces declension deviations more faithfully. These results underscore both the potential and limitations of Whisper and suggest directions for improvement, such as fine-tuning ASR models on learner corpora and integrating morphosyntactic analysis.\
**Keywords:** interlanguage, automatic speech recognition (ASR), Whisper, Polish, transcription, second language acquisition (SLA), learner error analysis

## Introduction 

### General Presentation 

This thesis was carried out as part of an internship at the *Structures Formelles du Langage* laboratory within the Master's program in Natural Language Processing (*Traitement Automatique des Langues*) at Inalco. The primary objective of this work is to conduct a thorough analysis of automatic tools in the context of Polish interlanguage, as produced by learners during second language acquisition. While automatic speech recognition (ASR) systems have achieved remarkable accuracy for standard languages, their application to second language production remains challenging. Learners' productions often exhibit variations that differ from those of native speakers, which standard ASR systems are not trained to recognize. Nevertheless, ASR offers promising possibilities for the transcription of learner interlanguage.

### Objectives 

This research is structured around two main objectives. The first objective is a qualitative linguistic analysis of learners' productions. Upon completion of corpus processing and extraction of learners' utterances, the study aims to identify the most frequent types of errors produced by adult learners of Polish after approximately 14 hours of instruction. An additional goal is to investigate the influence of learners' native languages on error patterns, determining whether specific trends can be observed among groups sharing the same mother tongue.

The second objective is the evaluation of the Whisper system's performance in transcribing Polish interlanguage. A key goal is to ensure that Whisper produces faithful transcriptions of learner speech, capturing the interlanguage exactly as spoken, including all deviations, errors, and disfluencies. This assessment examines the extent to which Whisper can accurately reflect learner utterances, while categorizing the types of outputs the system introduces. The qualitative analysis of these renderings will inform the limitations and strengths of Whisper in this context. Ultimately, the findings of this thesis aim to support potential adaptations to Whisper's architecture, enhancing its ability to transcribe Polish interlanguage precisely as articulated by the learner, thereby providing a reliable tool for second language acquisition research.

# General Context

## Context 

### Introduction

This section outlines the theoretical and empirical foundations relevant to the present study. It introduces the concept of interlanguage in second language acquisition, outlines the key linguistic features of Polish relevant for learners, and presents the VILLA project, which constitutes the source of the learner corpus analyzed in this thesis. Together, these elements establish the linguistic, cognitive, and pedagogical context in which the automatic transcription and error analysis of Polish interlanguage is conducted.

### Interlanguage in Second Language Acquisition

#### Definition of Interlanguage

*Interlanguage* is a concept introduced by [@selinker-1972] to describe the linguistic system that emerges when an adult learns a second language. It refers to a transitional linguistic system developed by the learner to communicate in the target language. This system is shaped by several factors, including the target language and the learner's native language [@tarone-2006]. In other words, interlanguage represents a transitional stage situated between the target language -- through the partial application of its lexical items and grammatical rules -- and the native language, from which the learner may potentially transfer previously acquired structures and patterns. As a result, interlanguage is typically marked by a high frequency of variations from the norm [@tarone-2006], reflecting its evolving and dynamic nature.

![Diagram of Interlanguage (Source: [@selinker-1972])](photos/interlanguage.png)

### Key Features of the Polish Language for Learners

#### Phonetics and orthography

Polish belongs to the family of West Slavic languages [@bartnicka-1990]. It uses the Latin alphabet, enriched with special diacritical marks and with double letters pronounced as one sound [@foland-2007].\
The Polish alphabet has 32 letters:



Below are selected letters that may present particular pronunciation challenges for non-native speakers:

::: 
   **Upper case**   **Lower case**    **IPA**    **Example**
  ---------------- ---------------- ------------ -----------------------------------------------------------------
         Ą                ą          /ɔŋ/, /ɔ̃w̃/  łąka /wɔŋka/ (\"meadow\"), szkołą /ʂkɔwɔ̃w̃/ (\"school\", Instr.)
         C                c             /t͡s/     taca /tat͡sa/ (\"plate\")
         Ć                ć             /t͡ɕ/     kochać /kɔxat͡ɕ/ (\"to love\")
         Ę                ę          /ɛŋ/, /ɛ̃w̃/  ręka /rɛŋka/ (\"arm\"), szkołę /ʂkɔwɛ̃w̃/ (\"school\", Acc.)
         J                j             /j/      pająk /pajɔŋk/ (\"spider\")
         K                k             /k/      sklep /sklɛp/ (\"store\")
         Ł                ł             /w/      koło /kɔwɔ/ (\"circle\")
         Ń                ń             /ɲ/      koń /kɔɲ/ (\"horse\")
         Ó                ó             /u/      król /krul/ (\"king\")
         Ś                ś             /ɕ/      śruba /ɕruba/ (\"bolt\")
         U                u             /u/      drut /drut/ (\"wire\")
         W                w           /v/, /f/   woda /vɔda/ (\"water\"), konewka /kɔnɛfka/ (\"watering can\")
         Y                y             /ɨ/      ryba /rɨba/ (\"fish\")
         Ź                ź           /ʑ/, /ɕ/   źrebię /ʑrɛbjɛ̃w̃/ (\"colt\"), gryźć /ɡrɨɕt͡ɕ/ (\"to bite\")
         Ż                ż           /ʐ/, /ʂ/   żaba /ʐaba/ (\"frog\"), wąż /vɔ̃w̃ʂ/ (\"snake\")

  : Selected Polish letters and their IPA transcriptions
:::

In addition, Polish includes several digraphs -- graphic combinations of two letters that represent a single sound [@foland-2007]:

::: 
   **Upper case**   **Lower case**    **IPA**    **Example**
  ---------------- ---------------- ------------ ------------------------------------------------------------------
         Ch               ch            /x/      chata /xata/ (\"hut\")
         Cz               cz            /t͡ʂ/     czysty /t͡ʂɨstɨ/ (\"clean\")
         Dz               dz         /d͡z/, /t͡s/  dzwon /d͡zvɔn/ (\"bell\"), powiedz /pɔvjɛt͡s/ (\"say\", imp., 2sg)
         Dź               dź         /d͡ʑ/, /t͡ɕ/  dźwięk /d͡ʑvjɛŋk/ (\"sound\"), powódź /pɔvud͡ʑ/ (\"flood\")
         Dż               dż            /d͡ʐ/     dżem /d͡ʐɛm/ (\"jam\")
         Rz               rz          /ʐ/, /ʂ/   rzeka /ʐɛka/ (\"river\"), malarz /malaʂ/ (\"painter\")
         Sz               sz            /ʂ/      kosz /kɔʂ/ (\"basket\")

  : Polish digraphs and their IPA transcriptions
:::

One of the more challenging aspects of learning Polish is its pronunciation. The language contains phonemes that are not present in other widely spoken Western languages, even if some may appear similar. Moreover, the frequent occurrence of complex phoneme clusters (difficult sounds placed directly next to each other) further complicates pronunciation for learners attempting to articulate Polish words accurately.

#### Morphosyntax: Case System

One of the greatest grammatical challenges in the Polish language is the inflection of words for case. Case is an inflectional category with a textual function, used to signal the grammatical relationships between elements of a sentence. In Polish, we distinguish seven forms of cases:\

-   Nominative -- Nominativus (Nom.),

-   Genitive -- Generativus (Gen.),

-   Dative -- Dativus (Dat.),

-   Accusative -- Accusativus (Acc.),

-   Instrumental -- Instrumentalis (Instr.),

-   Locative -- Locativus (Loc.),

-   Vocative -- Vocativus (Voc.).

Parts of speech that are conjugated by cases are nouns, adjectives, numerals, and pronouns.\
Below is an example of the declension of a Polish word -- *sklep* (store) -- depending on its syntactic role within a sentence:

::: 
     **Case**     **Singular**    **Plural**   **Question (function)**
  -------------- -------------- -------------- -----------------------------------------------------
    Nominative       sklep        sklep**y**   who? what? -- subject
     Genitive      sklep**u**    sklep**ów**   of whom? of what? -- possession, negation
      Dative      sklep**owi**   sklep**om**   to whom? to what? -- indirect object
    Accusative       sklep        sklep**y**   whom? what? -- direct object
   Instrumental   sklep**em**    sklep**ami**  with whom? with what? -- means or accompaniment
     Locative     sklep**ie**    sklep**ach**  where? about whom? about what? -- location or topic
     Vocative     sklep**ie**     sklep**y**   O! -- direct address

  : Declension of the noun \"sklep\" in Polish
:::

However, the case system does not end with just seven suffixes. The inflectional forms of nouns also depend on grammatical gender. Every noun has a gender: masculine, feminine, or neuter. The choice of endings is influenced by phonetic factors (such as whether the noun stem ends in a hard or soft consonant, or a vowel) as well as semantic factors (such as the category of animacy, inanimacy, and personal vs. non-personal reference within the masculine gender) [@bartnicka-1990].

### The VILLA Project

#### Structure and Goals

The project VILLA (\"Varieties of Initial Learners in Language Acquisition: Controlled classroom input and elementary forms of linguistic organisation\") conducted by [@dimroth-2013], investigated the initial stages of foreign language acquisition under controlled input conditions. In second language acquisition research, input refers to the language learners are exposed to in the target language, which provides the primary source of linguistic data for developing their interlanguage system. The study involved complete beginners from five different linguistic backgrounds -- Dutch, English, French, German, and Italian -- who each received 14 hours of instruction in Polish as a foreign language.

The project consisted of Polish language classes delivered by native Polish teachers, with communication-based methods. For each language group, two subgroups of up to 20 participants were formed, with members sharing similar profiles in terms of age, linguistic background, and field of study. All adult participants were university students, and none had any prior knowledge of Polish or another Slavic language [@dimroth-2013].

The classes were monolingual and learners were not allowed to take notes or consult additional sources of information. Instruction relied on visual aids such as presentations with pictures, recordings of dialogues and short video clips. The input was delivered in interactive and relatively natural conditions, and all sessions were recorded and transcribed for detailed analysis [@dimroth-2013].

As previously mentioned, each native language group was divided into two subgroups, receiving different types of input: one meaning-based and the other form-based. Learners exposed to meaning-based input received only structured input focused on communication, without any meta-linguistic explanations or explicit correction. Overall, the teacher did not prompt learners to reflect on language forms. In contrast, learners who received form-based input were explicitly directed to notice morphological forms and rules [@dimroth-2013].

#### Description of the Task

At the end of the course, the students' language skills were tested, during which they had to speak in Polish independently (without any help). One of the tasks, called *Route Direction*, required students to give directions from point A to point B using a map. The same map was used for all participants and included named streets and visual representations of places such as a hospital, school, restaurant, store, etc.



The oral productions during these tests were recorded and later transcribed. These transcriptions constitute the corpus we used in this work.

### Conclusions

This chapter established the theoretical and empirical foundations of the study. It introduced the concept of interlanguage as a transitional system shaped by both the target language and the learner's native language, highlighting its systematic and specific nature in adult second language acquisition. The discussion of Polish phonetics and morphosyntax emphasized the particular challenges posed by complex consonant clusters, nasal vowels, and the highly inflected case system, which together account for many learner difficulties. Finally, the presentation of the VILLA project and the Route Direction task provided the methodological framework on which the corpus of this thesis is based. Together, these components justify a detailed investigation of learner language patterns and the potential of automatic tools to process interlanguage data.

## State of the Art 

### Introduction

Automatic Speech Recognition (ASR) has undergone remarkable progress in recent decades, evolving from early systems limited to a small set of commands to deep learning--based models capable of handling spontaneous, continuous speech in real-world conditions. While ASR technologies are now widely applied in domains such as virtual assistants, customer service, and accessibility tools, their use in second language (L2) learning and assessment still requires careful evaluation of their performance.

### Automatic Speech Recognition for L2 Speech

ASR systems are trained on native speech and tend to perform poorly with non-native input, which can result in lower transcription accuracy and inaccurate evaluations of learner speech. For example, the system might produce incorrect text or suggest pronunciation corrections that do not match the learner's actual production, potentially providing misleading guidance. However, continuous improvements in machine learning and the increasing availability of diverse speech data have significantly reduced the accuracy gap between native and non-native recognition (e.g., Google ASR reduced this gap from 20% to 3--5%) [@gottardi; @https://doi.org/10.1002/tesq.3006].

Recent research highlights both the potential and the challenges of using automatic speech recognition (ASR) for pronunciation training. [@michot2024errorpreservingautomaticspeechrecognition] addressed the crucial issue of designing an ASR system that not only transcribes learner speech accurately but also preserves their errors, thus enabling effective corrective feedback. To this end, they collected approximately 85 hours of spontaneous English speech from Swiss learners in grades 4--6 (about 45,000 utterances) and manually transcribed it with explicit error annotations. They proposed a new evaluation metric, the Word-Based Error Preservation Rate (WEPR), to measure the extent to which ASR systems maintain learner errors instead of automatically "correcting" them. Their findings demonstrated that a fine-tuned ASR model, trained directly on children's data, achieved a substantially higher WEPR and lower Word Error Rate (WER) than off-the-shelf systems, underscoring the promise of error-preserving ASR for pedagogical purposes.

However, other work has pointed to the persistent limitations of existing ASR tools in real learning contexts. For instance, [@john2022] examined the case of *th*-substitution (e.g., *thank* $\rightarrow$ *tank*) among Quebec francophones learning English. In their study, eight participants (four female, four male) recorded 120 sentences with /$\theta$/-, /h/-, and vowel-initial words in both correct and erroneous forms, resulting in 480 recordings processed through Google Translate's ASR. While correct pronunciations were generally well recognized (75% for real-word and 83% for nonword contexts), erroneous productions were often misrepresented: only 25% of *thank* $\rightarrow$ *tank* substitutions were correctly identified, and in nearly half of the cases, the system misleadingly transcribed *tank* as *thank*. These findings illustrate the risk of false positive feedback, where ASR masks learners' mispronunciations, thus limiting its reliability. Together, the two studies highlight that while error-preserving ASR holds considerable promise for pronunciation pedagogy, mainstream tools such as Google Translate still struggle with systematic L2 pronunciation errors, demonstrating the need for tailored systems trained on learner-specific data.

Building on this line of inquiry, [@elayari:hal-04769687] evaluated Whisper on a longitudinal French L2 learner corpus and found that, although the system achieved relatively good WER and CER scores on advanced learners, it often "hyper-normalized" learner speech by correcting errors (e.g., *expériencer* $\rightarrow$ *expérimenter*), introducing hallucinations, or omitting disfluencies such as repetitions and pauses. This tendency compromises the reliability of ASR as a tool for SLA research, since deviations from the target norm are precisely the phenomena under investigation. At the same time, the authors note that ASR performance improves with learner proficiency, suggesting that error rates may indirectly reflect acquisition progress. They conclude that learner corpora should be conceptualized as a low-resource language variety and that fine-tuning ASR models on such data is crucial to ensure faithful transcription and avoid overcorrection.

#### Automatic Speech Recognition for L2 Polish Speech

Research on ASR for Polish, particularly for non-native speech, remains limited compared to English. The Polish language presents unique challenges for automatic recognition due to its rich inflectional system, free word order, and complex phonetic features, including nasal vowels, consonant clusters, and palatal fricatives [@zioko11_interspeech]. These linguistic characteristics make both accurate transcription and error detection in learner speech considerably more difficult than in less morphologically complex languages.

One of the earliest Computer-Assisted Pronunciation Training (CAPT) systems for Polish, AzAR, was developed specifically for German learners and combined HMM-based ASR with error patterns typical of L2 Polish [@wagner2010]. This system successfully helped learners identify and practice problematic contrasts(e.g., /ɕ/, /ʐ/, nasal vowels), and nasal vowels, demonstrating the potential of ASR-assisted feedback in targeted pronunciation training. However, AzAR faced limitations in recognition accuracy and robustness, particularly when handling spontaneous or less controlled speech.

More recently, end-to-end deep learning approaches, such as Whisper and wav2vec2, have opened new possibilities for Polish ASR. These models offer robustness across domains and the capacity to learn complex acoustic patterns directly from data. A promising direction is the fine-tuning of such large models on learner-specific corpora, like EURONOUNCE [@cylwik09_slate], which contains non-native Polish speech. Fine-tuning on these datasets could ensure that interlanguage features are preserved in the transcription rather than automatically normalized, thus providing more accurate feedback and enabling detailed analysis of learner errors.

### The Whisper Model

Whisper [@radford2022robustspeechrecognitionlargescale] represents a new generation of ASR: a transformer encoder--decoder trained on 680,000 hours of multilingual data. Unlike traditional HMM-based systems, Whisper directly predicts text tokens from log-Mel spectrograms, offering robustness across domains, languages, and accents. Models are released in multiple sizes, enabling a balance between speed and accuracy.

For L2 speech, Whisper performs better than many commercial systems, but it often \"over-corrects\" learner speech -- for example, restoring omitted particles or ignoring disfluencies. This behavior, observed in L2 French [@elayari:hal-04769687], risks erasing the very interlanguage phenomena. In the context of Polish, such normalization could obscure substitutions of nasal vowels or partial palatalization.

Nevertheless, Whisper's open-source nature, high baseline accuracy, and multilingual scope make it an attractive candidate for adaptation. With targeted fine-tuning on learner corpora, it could become a powerful tool for L2 research.

### Morphosyntactic Analysis and Case Detection in NLP

Morphosyntactic analysis assigns grammatical categories, such as part of speech, case, number, and gender, to textual units. In highly inflected languages like Polish, this process is essential due to the complexity of declension and conjugation. Accurate morphosyntactic tagging supports various NLP tasks, including syntactic parsing, machine translation, and automatic error detection in language learning. In this study, *spaCy* was used for Polish morphosyntactic analysis, providing lemmatization, part-of-speech tagging, and morphological features, including case information, in a flexible and accessible framework.

Detecting grammatical cases in Polish remains challenging due to the language's rich inflectional system. Correct case identification is crucial for analyzing learner speech, as it helps preserve interlanguage features in ASR outputs rather than normalizing them. Although general research on morphosyntactic analysis is extensive, studies focusing on Polish are more limited. Previous works [@kuta2007; @pawlik-etal-2013-optimizing] evaluated tagging accuracy and proposed optimized algorithms for inflectionally rich languages, highlighting the need for tailored approaches. Despite progress, morphological ambiguity and syntactic complexity continue to pose challenges, motivating the integration of advanced neural models with ASR to improve recognition and analysis of learner errors.

### Conclusions

Automatic Speech Recognition has achieved remarkable progress, but accurately processing non-native speech remains a significant challenge. Systems trained on native input often misrepresent learner productions, either masking errors or providing misleading corrections. Recent research shows that error-preserving approaches, fine-tuned on learner data, can substantially improve both accuracy and the faithful representation of interlanguage features.

In the case of Polish, challenges are even greater due to rich morphology, free word order, and complex phonetics. Early systems demonstrated potential but lacked robustness, while modern end-to-end models like Whisper risk excessive normalization. Moving forward, progress depends on adapting large ASR models through fine-tuning on learner corpora and combining them with morphosyntactic analysis, ensuring that learner-specific patterns are captured rather than erased. Such tailored approaches hold promise for advancing research on non-native speech.

# Experimentations

## Corpus 

### Introduction

This chapter presents the learner and native speaker data used in the study, as well as the preprocessing and annotation procedures applied. It describes the collection, transcription, and organization of recordings from the Route Direction task, detailing both manual and automatic processing steps. The chapter also explains the rationale behind the corpus design, including decisions regarding participant selection, data format, and handling of interlanguage-specific phenomena, in order to ensure a reliable and analyzable dataset for subsequent linguistic and ASR evaluation.

### Learner Corpus

The corpus used for the analysis consists of manual transcriptions of voice recordings from the Route Direction task. The transcriptions were created by the author of the thesis (a native speaker of Polish), using ELAN, a tool for annotating audio and video recordings, and saved in `.eaf` format. Each file include two parallel tiers:\

-   **\*STU**: manual transcriptions that accurately reflect what the learner said;

-   **%pol**: corrected versions in standard Polish, representing the intended meaning of the learner's utterance.

The corpus analysed in this study includes only data from the meaning-based groups across all five countries. This decision was made due to the limited availability of recordings from the form-based groups, as well as the intention to maintain a balanced dataset for each language group. Furthermore, the analysis is restricted to adult learners, as the data from the group of children (Germany) was also limited.

For each country, the corpus includes the same types of data: audio recordings (`.wav` files), manual transcriptions (`.eaf` files), and automatic transcriptions generated by Whisper (`.txt` files).

::: 
  **Country**    **Number of wav/eaf/txt files**  **Total duration of recordings**
  ------------- --------------------------------- ----------------------------------
  France                       17                 23 minutes 32 seconds
  Italy                        17                 26 minutes 39 seconds
  Netherlands                  18                 28 minutes 34 seconds
  England                      17                 29 minutes 34 seconds
  Germany                      20                 30 minutes 42 seconds

  : Summary of recordings by country
:::

As previously mentioned, Polish is a relatively difficult language to acquire, especially for learners with no prior exposure to Slavic languages. One of the primary challenges lies in its phonological system, which includes numerous sounds absent in many other languages. Another major difficulty is its grammar, especially the complex system of case inflection. After only 14 hours of study, it is expected that learners will produce numerous errors. The aim of this study is to faithfully represent these mistakes in order to contribute to improving the quality of foreign language instruction.

It is important to note that all segments were transcribed in accordance with standard Polish orthographic norms. Consequently, pronunciation errors were indicated through Polish spelling rather than phonetic transcription using the International Phonetic Alphabet (IPA). For instance:

::: 
         **\*STU**        **%pol**
  ----------------------- -----------------------
   za **sz**klepe (\...)  za **s**klepem (\...)

  : Example forms
:::

In this example, the learner replaced the voiceless alveolar fricative /s/ in the instrumental form of the word *sklep* with the retroflex /ʂ/, represented in Polish orthography by the digraph *sz*. Additionally, the final /m/ was omitted.\
There are a few reasons why the recordings were transcribed in accordance with standard Polish orthography instead of the phonetic alphabet. Firstly, manual transcription is a very tedious and time-consuming process that requires a lot of attention. Consequently, the annotation rules should be as simple and intuitive as possible [@Grochola-Szczepanek_Woźniak_2018]. In addition, full phonemic transcription using the IPA would have been significantly more time-consuming. Given the limited time, this would have led to a substantial reduction in the size of the corpus. Moreover, such transcription facilitates processing by automated tools. Only general orthographic transcription allows the use of tools such as lemmatization, part-of-speech tagging, grammatical case identification, and language detection, which are designed for standard orthography. Finally, the corpus and the analysis are intended for further work by other researchers in the laboratory, not only phoneticians and phonologists.

Nevertheless, in the subsequent analysis of phonetic errors, the orthographic representations were automatically converted into IPA symbols to enable a more precise visualization of pronunciation deviations.

The same task was also carried out by four native Polish speakers, whose utterances were recorded and transcribed following the same procedure as for the learner corpus. While this native speaker corpus is significantly smaller in size, it serves as a reference point for the subsequent evaluation of the performance of automatic linguistic tools.

### Annotation and Preprocessing

#### Tools and Implementation

All scripts developed in this thesis were implemented in Python within a Jupyter Notebook environment. For the automatic speech recognition of learners' utterances, we used the small model of Whisper by OpenAI, in automatic language mode, provided by Huma-Num servers, since Polish was not available.

The implementation further relied on a range of Python libraries, including *spaCy* for morphosyntactic analysis, *pandas* for data manipulation, *fuzzywuzzy* (Levenshtein distance) for fuzzy string matching, *Epitran* for grapheme-to-phoneme transcription, *langdetect* for language detecting, *matplotlib* and *seaborn* for visualization, *JiWER* for calculating WER and CER, as well as *json*, *xml.etree*, and *csv* for structured data processing and file management.

This configuration ensured reproducibility and scalability, while enabling the efficient integration of data processing, linguistic analysis, and evaluation procedures.

#### Manual Preprocessing

During the task, teachers typically did not contribute to the learners' utterances. However, the learners' recordings of the task always began with a teacher who asked for the student's identifier and then gave a brief introduction to the task in Polish:\
*We are here at the train station in Kraków. I'm a tourist from Warsaw, and you live in Kraków. I, the tourist, am asking for information. Excuse me, how can I get to 4 Dobra Street?*\
At the end of each recording, they thanked the learner and made brief encouraging remarks, such as \"very good,\" etc.

All teacher utterances were excluded from the corpus, as the analysis focuses solely on the learners' interlanguage. Since the transcriptions of these utterances were not identical, automatically removing them would have been difficult. Therefore, the teachers' speech at the beginning and end of each recording was removed manually.

Another challenge in the corpus was the presence of words in the learners' native languages, which were sometimes produced during the recordings. These fragments were also initially transcribed, but they complicated the comparison between the automatic and manual transcriptions, as well as the analysis of learner errors.

To address this issue, a function was created to automatically detect words belonging to the native languages of the learners involved in the project (French, Italian, English, German, and Dutch), using the *langdetect* library.\
**Results:**\
`’de’: [’ich’, ’ichś’, ’uniwersitet’, ’uniwersiteć’, ’uniwersytet’, ’uniwerszitet’, ’uniweszitet’], ’nl’: [’en’, ’juniwersitet’, ’juwersytet’], ’it’: [’aller’, ’allora’, ’dicevi’, ’il’, ’ne’, ’ospitalem’, ’quattro’, ’spita’, ’spital’, ’spitala’, ’spitalem’, ’szpitale’, ’tiatr’, ’ulicon’], ’fr’: [’desolée’, ’du’, ’es’, ’est’, ’le’, ’oublié’, ’oui’, ’où’, ’plus’, ’questo’, ’tourner’], ’en’: [’ctery’, ’o’, ’teatr’, ’teatry’, ’to’, ’tourner’]`\
At this point, the corpus was not yet complete; however, the preliminary results showed that the majority (66%) of the words detected as belonging to another language were in fact erroneous forms from the learners' Polish interlanguage. Although some words were correctly classified (in bold), they remained a minority. Unfortunately, as many words from the \*STU segments were simplified attempts at Polish words, the program sometimes incorrectly classified them as belonging to other languages.

To allow for comparison with the native Polish corpus, the same language detection library was applied to the transcriptions produced by the four native speakers. Out of a total of 96 words, only one word -- the Polish word *teraz* (\"now\") -- was mistakenly identified as Italian, representing just 1% of the data. This result confirms the overall reliability of the language detection tool and suggests that the challenges observed in the learner corpus are primarily due to the deformed nature of interlanguage forms rather than limitations of the library itself.

This demonstrates that the automatic method was unreliable. As a result, the removal of non-Polish words had to be done manually.

#### Automatic Preprocessing

The automatic data‑processing workflow comprises a few successive stages. First, the code systematically traverses all corrected `.eaf` files. For each file, it retrieves the learner identifier together with every learner utterance (\*STU) and its corresponding corrected version in Polish (%pol). These elements are then compiled into an individual, well‑structured XML document that records the learner's ID, country of origin, and each pair of learner and target‑language statements (see [] for an example XML file).

The second stage focuses on the automatic transcriptions stored as `.txt` files. The function first verifies that the content is indeed Polish; non-Polish segments are named differently in the final file. Out of 89 examples, 15 were generated in a language other than Polish. These hallucinations are caused by the highly distorted nature of the interlanguage, as well as by rare instances where some learners briefly switched to their native language.

The program subsequently normalises the remaining text by converting it to lower case, removing all punctuation except hyphens, and eliminating superfluous whitespace.

During the enrichment phase, the procedure aligns each cleaned automatic transcription with its counterpart XML file, matching them by filename. For every resulting entry it records the learner number, the country, the automatic transcription, and the full set of manual transcriptions together with their Polish corrections, each labelled with its segment number. This step yields a comprehensive dataset that integrates all available sources.

Finally, the entire enriched corpus is exported to a single JSON file (see [] for an example fragment of the JSON file). This consolidated resource provides an organised view of the data, thereby facilitating subsequent quantitative and qualitative analyses.

In addition, to facilitate the technical processing of the corpus, a script was developed that creates a dictionary grouping words according to their lemmas. It begins by extracting all the correct Polish versions from the dataset and lemmatizing them using the *spaCy* library -- including stopwords, which are also relevant for the analysis since learners sometimes produce distorted forms of these frequent function words. The resulting lemmas are stored in a sorted list.

In the next step, a complete corpus is assembled by combining the automatic transcriptions, manual transcriptions, and the corrected Polish versions. This extended corpus is also lemmatized, and a sorted list of all lemmas is generated.

To identify potentially unknown or erroneous word forms, the script compares the lemmas from the complete corpus with those from the correct Polish data. It then groups together words that belong to the same lemma. Unmatched forms are extracted and aligned with the closest known lemmas using Levenshtein distance. These alignments are stored in a dictionary that merges all words -- both the correct forms and those matched by similarity, while avoiding duplicates (see  [] for an example of a group of words associated with the same lemma).

It is important to note certain limitations of the automatic alignment process. Some words could not be matched due to significant distortions produced by learners, which complicates accurate lemma alignment. The short length and limited phonetic richness of stopwords further challenge their automatic grouping. Moreover, stopwords are sometimes confounded with hesitations or interrupted word attempts (e.g., \"skre\" preceding the word *skręcić* is treated as a distinct word), which adds to the complexity of alignment. The final dictionary contributes to the subsequent automatic segmentation of the learners' transcriptions.

### Conclusions

This chapter described the composition and preparation of the corpora that form the basis of the present study. The learner corpus, derived from the VILLA project, was carefully transcribed and annotated to reflect both the learners' productions and their corrected Polish counterparts, amounting to a total of 89 files and 2 hours and 19 minutes of recordings, while the smaller native speaker corpus serves as a comparative benchmark. The annotation and preprocessing pipeline, combining manual and automatic procedures, allowed for the integration of multiple sources of data into a consolidated JSON file enriched with lemma-based alignments. Despite certain limitations (such as the difficulty of automatically detecting highly distorted forms) the resulting dataset provides a robust and structured resource for subsequent analyses. Overall, the corpora and their preparation ensure a reliable foundation for the evaluation of linguistic errors and the performance of automatic tools such as Whisper in processing Polish interlanguage.

## Qualitative Linguistic Analysis 

### Introduction

The first analysis conducted in this study focused on the non-standard forms made by learners. The primary objective was to identify the most common types of deviations produced by learners of Polish after a 14-hour course. In addition, the second goal was to investigate the potential influence of the learners' native languages on the nature of these productions. To facilitate a clearer visualization of deviations, a dedicated tool-platform will also be developed, enabling an easier and more systematic analysis of the data.

### Classification of Deviations

#### Introduction

The nature of the task allowed for the classification of learner errors into two main categories: declension errors (i.e., incorrect grammatical case inflections) and pronunciation errors. Since the learners were reproducing utterances they had previously heard and repeated after native Polish speakers -- rather than learning grammatical rules or case endings by heart -- their erroneous forms typically stem from either inaccurate pronunciation or misusage of case endings.

### Corpus Processing for Extraction of Deviations

In order to systematically identify and extract learner errors from the corpus, an automatic alignment procedure was implemented to compare learners' manual transcriptions with their corresponding correct Polish versions at the word level. The script performs an automatic word-by-word alignment between learners' manual transcriptions and their corresponding correct versions in Polish. First, it loads the processed and organised transcription data as well as the dictionary with words associated with lemmas. Based on this dictionary, the script builds a reverse mapping from word forms to their most frequent lemmas. For each pair of utterances (manual transcription and correct version), the script attempts to align the words by comparing their lemmas. If no lemma match is found, it falls back on fuzzy string matching to identify the most likely corresponding word, using a similarity threshold. Each aligned pair of words is saved into a structured format, including the learner ID, country, and aligned segments. The final output is a JSON file containing the aligned word pairs, which are the base for further error analysis (see  [] for an example of a segment with pairs of words from the manual transcription and the corresponding correct version).

Out of 4,178 words in the manual transcriptions, 3,466 were successfully aligned with their correct counterparts, accounting for 82.96% of the manual transcription corpus.

The next step was the extraction of the erroneous words, i.e. the pairs where the word from the manual transcription differs from the corresponding correct version. To achieve this, a script was written to process the JSON file containing aligned segments for each learner. For every pair of words, the script checks whether both manual and correct forms are present and different. If so, the error is registered along with the learner ID and their country. To avoid double-counting, each unique error per learner is stored only once. The results are then grouped by correct form, incorrect (manual) form, and country, and saved into a CSV file listing the number of learners per country who made each error, along with their IDs. In addition, global statistics are computed to count the total number of aligned word pairs and how many of them contain an error.

  **Correct form**   **Erroneous form**    **No. of learners**   **FR**   **IT**   **NL**   **UK**   **GE**  **Learners**
  ------------------ -------------------- --------------------- -------- -------- -------- -------- -------- --------------------
  iść                idź                            5              5        0        0        0        0     1104, 1108, (\...)
  iść                iś                            25              2        8        3        11       1     1115, 1118, (\...)
  iść                iszcze                         1              1        0        0        0        0     1117
  iść                iścz                           1              1        0        0        0        0     1117
  iść                isze                           1              0        1        0        0        0     5109

  : Excerpt with correct and erroneous forms and learner distribution

Out of 3,466 aligned pairs, 1,352 were identified as erroneous, accounting for 39.01% of the data. This corpus serves as the foundation for the subsequent analysis of learners' errors.

### Declension Deviations

Although the utterances were relatively short, they often required the use of correctly inflected forms.

::: 
  **EN**                                                   **PL (Nom.)**                                                       **PL correct**                                                       **Case**
  -------------------------------------------------------- ------------------------------------------------------------------- -------------------------------------------------------------------- --------------
  go straight on Niska Street                              idź prosto \[ulic**a** Nisk**a**\]                                  idź prosto ulic**ą** Nisk**ą**                                       instrumental
  behind the hospital                                      za \[szpital\]                                                      za szpita**lem**                                                     instrumental
  turn right into Juliusz Słowacki Street                  skręć w prawo w \[ulic**a** Juliusz Słowacki\]                      skręć w prawo w ulic**ę** Juliusz**a** Słowacki**ego**               accusative
  next to the restaurant, library, school and university   obok \[restauracj**a**, bibliotek**a**, szkoł**a**, uniwersytet\]   obok restauracj**i**, bibliotek**i**, szkoł**y**, uniwersytet**u**   genitive
  behind the store                                         za \[sklep\]                                                        za sklep**em**                                                       instrumental
  turn left into Dobra Street                              skręć w lewo w \[ulic**a** Dobr**a**\]                              skręć w lewo w ulic**ę** Dobr**ą**                                   accusative
  the Kowalski family's house                              dom \[Kowals**cy**\]                                                dom Kowalski**ch**                                                   genitive

  : Examples of Polish case usage in route directions
:::

#### Corpus Processing

In order to identify words with errors related to declension, only nouns, adjectives, numerals, and pronouns must be taken into consideration, as these parts of speech are inflected for case. Using the Polish language model from the *spaCy* library, the script extracts all such words from the \"Correct form\" column, along with the corresponding data from each row. Since the corpus does not contain any numerals or pronouns, only nouns and adjectives were extracted, resulting in 306 examples.

Next, the script processes each pair of incorrect and correct forms using *spaCy* to identify the grammatical case of each word and compare the two forms. Each error is recorded, along with an indication of whether the grammatical cases match or differ. The results are then saved to a new CSV file.

  **Erroneous form**   **Case**   **Correct form**   **Correct Case**   **Corr.**    **FR**   **IT**   **NL**   **UK**   **GE**
  -------------------- ---------- ------------------ ------------------ ----------- -------- -------- -------- -------- --------
  ulicza               Gen        ulicą              Ins                different      2        0        7        2        1
  ulisa                Acc        ulicą              Ins                different      1        0        0        1        0
  ulica                Nom        ulicą              Ins                different      10       6        5        5        4
  ulice                Acc        ulicą              Ins                different      1        1        0        0        0
  ulika                           ulicą              Ins                different      2        0        0        1        0

  : Excerpt of forms with grammatical cases, correspondence, and learner distribution by country

Nevertheless, the automatic identification of grammatical cases presents certain limitations. Firstly, in the context of interlanguage, the system may assign incorrect cases due to the presence of non-standard or unrecognised forms that are not part of the Polish lexicon. Secondly, the Polish case system itself is highly complex -- a single inflected form may correspond to multiple cases. As a result, accurately identifying the correct case often requires considering the broader syntactic context of the word within the sentence.

For this reason, the table was manually corrected and saved as a new CSV file for the subsequent evaluation of *spaCy* in case attribution.

Next, all examples with the word \"identical\" in the \"correspondence\" column or with empty values were removed from the table to create a corpus consisting solely of incorrect inflections. Consequently, the final table contains 204 examples.

#### Evaluation of *spaCy* in Case Attribution

An evaluation of *spaCy*'s performance in case detection was conducted separately for the incorrect learner forms and their corrected counterparts. The results show that *spaCy* achieved 60% accuracy on the incorrect forms and 75% accuracy on the corrected forms.

  **Case**                           **Precision**    **Recall**   **F1-score**   **Support**
  --------------------------------- ---------------- ------------ -------------- -------------
  *Evaluation on erroneous cases*                                                
  Acc                                     0.38           0.40          0.39           20
  Dat                                     0.00           0.00          0.00            0
  Gen                                     0.60           0.59          0.60           61
  Ins                                     0.75           0.55          0.63           22
  Loc                                     0.00           0.00          0.00           21
  Nom                                     0.74           0.73          0.73           142
  nan                                     0.10           0.50          0.16            6
  **Accuracy**                       **0.60** / 272                              
  **Macro avg**                           0.37           0.39          0.36           272
  **Weighted avg**                        0.61           0.60          0.60           272
  *Evaluation on correct cases*                                                  
  Acc                                     1.00           1.00          1.00           23
  Dat                                     0.00           0.00          0.00            0
  Gen                                     0.90           0.65          0.75           162
  Ins                                     0.73           1.00          0.85           74
  Loc                                     0.00           0.00          0.00           13
  Nom                                     0.45           1.00          0.62           29
  nan                                     0.00           0.00          0.00            5
  **Accuracy**                       **0.75** / 306                              
  **Macro avg**                           0.44           0.52          0.46           306
  **Weighted avg**                        0.77           0.75          0.74           306

  : Classification metrics for erroneous and correct forms by grammatical case

To better understand whether these difficulties stem from interlanguage or from the complexity of the language itself, the same procedure was applied to the small Polish native corpus. The overall accuracy in this case was only 67%, which falls between the scores observed for learner errors and corrected forms.

  **Case**            **Precision**   **Recall**   **F1-score**   **Support**
  ------------------ --------------- ------------ -------------- -------------
  Acc                     1.00           0.50          0.67            2
  Dat                     0.00           0.00          0.00            0
  Gen                     0.25           0.67          0.36            3
  Ins                     0.86           1.00          0.92            6
  Loc                     0.00           0.00          0.00            7
  Nom                     0.79           0.94          0.86           16
  UNK                     0.00           0.00          0.00            2
  **Accuracy**        **0.67** / 36                              
  **Macro avg**           0.41           0.44          0.40           36
  **Weighted avg**        0.57           0.67          0.60           36

  : Classification metrics for a Polish native dataset by grammatical case

The first two results suggest that the interlanguage nature of the data is a significant factor affecting *spaCy*'s performance in case detection; particularly in instances where errors impact the word's suffix due to pronunciation deviation (e. g. *niskon* /ɲiskɔn/ instead of *niską* /ɲiskɔ̃w̃/). However, the tool also struggles with correctly analysing native Polish utterances. It appears that the complexity of the Polish case system itself poses a great challenge for the tool, as well. Consequently, it may be beneficial in future work to incorporate a broader syntactic context by including a few words preceding each analysed token. This could help determine whether *spaCy*'s performance improves when given more linguistic context.

#### Results

  **Case**    **Expected cases**   **Produced cases**   **Difference (%)**
  ---------- -------------------- -------------------- --------------------
  Acc                 16                   13                 -18.75
  Gen                106                   5                  -95.28
  Ins                 59                   7                  -88.14
  Loc                 11                   19                 72.73
  Nom                 12                  125                 941.67

  : Comparison of expected and produced grammatical cases with relative differences (%)





The following analysis of learner data shows that the most frequently required cases, presented in Table  -- the genitive and instrumental -- also generate the highest number of errors among learners. The genitive case is typically used to express possession and appears frequently in phrases referring to street names, such as *ulica Juliusza Słowackiego* (\"Juliusz Słowacki Street\"). It also follows prepositions like *obok* (\"next to\" or, in this context, \"past\"), which are commonly used in giving directions. The instrumental case, on the other hand, is used when describing movement along a path, especially after verbs of motion such as *iść* (\"to go\"), as in *iść ulicą Niską* (\"go along Niska Street\"). It is also required after the preposition *za* (\"behind\"), which frequently appears in this route direction task.

Moreover, one of the most common incorrect cases used by learners is the nominative. This is not unexpected, as the nominative is the default case in Polish. It is the form learners are most familiar with, and in the absence of explicit knowledge about declension rules, they often overgeneralize and use the nominative in contexts that require a different case. This tendency reflects a typical stage in interlanguage development, where learners rely on the most salient or frequent forms of the target language.

In addition, heatmaps were generated to visualize the distribution of grammatical case errors, comparing the incorrect cases used by learners with the correct ones. Cells outlined in green correspond to correct case usage, but since such examples were excluded from the corpus at an earlier stage, these cells all show zero values.





From the first table (Figure []), we can confirm the previously mentioned observation that the nominative case is dominant among incorrect usages. Although the overall number of accusative and locative errors is relatively low, in most of these cases (around 80%), learners incorrectly used the nominative instead of the expected form. Similarly, both genitive and instrumental cases are frequently replaced by the nominative -- approximately 63% of the time -- though some of these errors also involve confusion between genitive, instrumental, and locative.

The locative case, which also appears to be slightly overused, is typically required after prepositions such as *na* (\"on\") or *w* (\"in\"). This overuse may stem from learners relying on familiar phrases and generalising them to contexts where other cases are expected. The characteristic suffixes of Polish cases (such as -*u*, -*e*, -*em*, or -*a*) can be particularly misleading for learners. For example, the phrase *obok szpitalu* instead of the correct *obok szpitala* (\"next to the hospital\") illustrates confusion between the genitive and locative, likely influenced by more frequent expressions like *w szpitalu* (\"in the hospital\"). In fact, 52.63% of incorrect uses of the locative occurred in contexts where the genitive case was required. Furthermore, 36.84% of the same locative errors involved confusion with the instrumental (*za szpitalem* (\"behind the hospital\")).

A similar pattern can be observed with accusative errors: 53.85% of incorrect accusative forms were used in contexts where the genitive was required, and 23.08% where the instrumental was expected. In such situations, learners may simply not recall the correct case and default to a form they have encountered more often or that sounds familiar.

These tendencies underscore the crucial role that morphological endings play in learner errors. The overlap of case endings, combined with limited exposure and overgeneralisation, leads to predictable yet systematic patterns of confusion in learners' oral productions.

Overall, there is little evidence to suggest that the learners' native language had a significant influence on their case-related errors. While some languages like German also feature grammatical cases, the structure and endings differ considerably from those in Polish. Even if certain similarities exist, they do not seem to systematically affect learners' performance in this corpus. Moreover, the pedagogical method used in this project is an important factor to consider: rather than learning through explicit grammar instruction and memorisation of case endings, students were primarily exposed to native speaker input and encouraged to repeat phrases. This focus on auditory learning may have reduced the potential for native language transfer. Although cross-linguistic influence cannot be entirely ruled out, the variation and nature of errors suggest that case-related difficulties arise more from the complexity of the Polish case system itself than from the influence of the learners' L1.

### Pronunciation Deviations

Another significant challenge for the learners was Polish pronunciation, mostly due to its complex consonant clusters and unfamiliar sounds. A clear example is the verb *skręcić* (\"to turn\"), which contains a consonant cluster at the beginning (*skr*-) that is difficult to articulate for many non-native speakers. Additionally, the nasal vowel *ę* and the soft *ć* at the end require precise articulation that may not exist in the learners' native phonetic systems. This combination of sounds makes words like *skręcić* particularly hard to pronounce accurately for beginners. Such pronunciation challenges often lead to distorted forms, contributing significantly to the deviations observed in interlanguage speech.

#### Corpus Processing

As for the analysis of errors connected to pronunciation, another script was developed in order to detect and extract phonetic differences between the erroneous and correct word forms.

The script first defines a set of Polish digraphs (*cz*, *sz*, *dz*, *dż*, etc.) and typical case-related suffixes (*ą*, *a*, *u*, *em*, etc.). Each word is then split into phonetic units, treating digraphs as single sounds. Suffixes that mark grammatical case endings are ignored. This helps isolate pronunciation issues from case-related morphological variation.

However, in some cases, phonetic errors occur specifically within the suffixes that indicate grammatical case endings. To address this, the script includes a function that identifies and removes such endings when a clear phonetic deviation is observed. For example, if the correct word ends in -*ą* (/ɔ̃w̃/) but the erroneous form ends in -*on* (/ɔn/), -*om* (/ɔm/), or -*o* (/ɔ/) -- all common mispronunciations of the nasal vowel *ą* -- the suffix is considered a phonetic error and excluded from the comparison.

In the next step, the *difflib* library is used to compare the segmented forms of the correct and incorrect words. For each word pair, only the differing letters are extracted and saved. Each difference is represented as a pair: the correct form and the erroneous form. Each difference is saved as a separate row in a table, alongside the number and origin of the learners who made the mistake.

The first attempt at grouping pronunciation errors was based on phoneme-level similarities. The code processes the previously prepared dataset containing pronunciation errors made by the learners. It groups all learners who produced the same error by creating a dictionary where each key is a (Correct, Incorrect) pair and the value is the set of learner IDs. A summary table is generated, listing the correct and incorrect forms, the number of learners from each country, the total number of learners for each error, and example words in which the error occurred.

::: 
   **Correct**   **Erroneous**   **FR**   **IT**   **NL**   **UK**   **GE**   **Total learners**  **Word examples**
  ------------- --------------- -------- -------- -------- -------- -------- -------------------- ----------------------------------------------------------------------------
       sz              s           7        7        7        10       16             47          juliusza, proszę, szkoły, szpitala, szpitalem
        ł              l           7        5        9        7        13             41          szkoły, słowackiego
        s             sz           2        12       11       7        3              35          niską, prosto, się, sklep, sklepem, sklepu, skręcisz, skręcić, słowackiego
        c             cz           4        3        13       3        6              29          restauracji, skręcić, stacji, słowackiego, ulica, ulicy, ulicą, ulicę
        ć             --           3        8        3        11       1              26          iść, skręcić

  : Excerpt: Distribution of correct vs. erroneous forms and example words per learner country
:::

Nevertheless, this way of presenting phonetic errors is not ideal. For future linguistic analysis, it is crucial to retain information about the specific words in which a given phonetic error occurred, as this can help identify underlying factors such as native language interference or target language influence. While in this representation we can see which words contained a particular phoneme error, it does not indicate whether all learners actually mispronounced those words. For instance, in the first example, one learner might have pronounced Juliusza correctly but made an error in proszę. Although this representation already offers some insights, it lacks precision and may not be sufficiently informative for in-depth phonetic analysis or error pattern discovery.

We developped a second method of grouping pronunciation errors involved organizing them by lemma in order to identify recurring mispronunciations of the same lexical item. For each entry, the script extracts the lemma of the correct form using the Polish *spaCy* model. Then, it groups all instances that share the same lemma, correct form, and corresponding erroneous pronunciation. Within each group, it aggregates the different correct and incorrect forms as well as the learner IDs associated with the error. As always, the script also shows the number of learners from each country and the total number of learners for each error.

In the second part, the code uses the *Epitran* library to convert all correct and erroneous forms into their phonetic representations. This results in a final file where all entries are transcribed in IPA, allowing for a more fine-grained analysis of recurring pronunciation patterns and errors across learners. Both representations are saved into new CSV files.

#### Results

::: 
  **Correct form(s)**   **Erroneous form(s)**    **Corr.**   **Err.**    **FR**   **IT**   **NL**   **UK**   **GE**  **Total learners**   **Learners**
  --------------------- ------------------------ ----------- ---------- -------- -------- -------- -------- -------- -------------------- --------------
  szkoły                skola, skole, (\...)     ł           l             4        5        6        7        10    32                   1108, (...)
  szpitala, szpitalem   spita, spitae, (\...)    sz          s             2        5        3        8        10    28                   1117, (...)
  iść                   iś                       ć           --            2        8        3        11       1     25                   1115, (...)
  cztery                sztere, szteri, (\...)   cz          sz            2        7        9        0        7     25                   1103, (...)
  szkoły                skała, skola, (\...)     sz          s             5        5        3        2        10    25                   1108, (...)

  : Excerpt of correct and erroneous forms with learner distribution by country
:::

::: 
  **Correct form(s)**   **Erroneous form(s)**   **Corr.**   **Err.**    **FR**   **IT**   **NL**   **UK**   **GE**  **Total learners**   **Learners**
  --------------------- ----------------------- ----------- ---------- -------- -------- -------- -------- -------- -------------------- --------------
  ʂkɔwɨ                 skɔla, skɔlɛ, (\...)    w           l             4        5        6        7        10    32                   1108, (...)
  ʂpitala, ʂpitalɛm     spita, spitaɛ, (\...)   ʂ           s             2        5        3        8        10    28                   1117, (...)
  iɕt͡ɕ                  iɕ                      t͡ɕ          --            2        8        3        11       1     25                   1115, (...)
  t͡ʂtɛrɨ                ʂtɛrɛ, ʂtɛri, (\...)    t͡ʂ          ʂ             2        7        9        0        7     25                   1103, (...)
  ʂkɔwɨ                 skawa, skɔla, (\...)    ʂ           s             5        5        3        2        10    25                   1108, (...)

  : Excerpt of correct and erroneous forms with learner distribution by country (IPA)
:::

These tables present the most frequent pronunciation errors made by the learners, based on a total of 310 examples. The \"base\" of each entry corresponds to the correct form of a word -- or multiple forms sharing the same lemma (e.g., different case-inflected variants of the same word). For each entry, the table includes the erroneous forms produced by the learners, the correct-erroneous sound pair, and the statistical data. This representation allows for a clearer understanding of how many learners from each country produced the same phonetic error within a given word.

The five most frequent pronunciation errors observed in the learner corpus reveal recurring patterns and potential phonological challenges, most likely influenced by the learners' native languages. The most common error concerned the substitution of the Polish phoneme /w/ (spelled *ł*) with /l/, particularly in the word *szkoły* /ʂkɔwɨ/, which was frequently realized as *skola* /skɔla/, *skole* /skɔlɛ/, *szkole* /ʂkɔlɛ/, and similar forms. This error was made by 32 learners across all language groups, with the highest number found among German speakers (10); however, all groups exhibited this error at some point. The second most common error involved the replacement of /ʂ/ with /s/ in the word *szpital* /ʂpital/, where learners produced forms such as *spita* /spita/ or *spytal* /spɨtal/. This suggests difficulty in distinguishing between retroflex and alveolar fricatives. Once again, German speakers accounted for the highest number of errors (10), while French learners made the fewest (2). A similar phenomenon appeared in the third error, where the affricate /t͡ɕ/ in the verb *iść* /iɕt͡ɕ/ was omitted, resulting in the simplified form *iś* /iɕ/, produced by 25 learners. This pattern may indicate difficulty pronouncing complex affricates in word-final position. Interestingly, the English group committed this error most frequently (11), whereas it was least common among German learners (1). The fourth error again reflected confusion between retroflex and alveolar consonants: *cztery* /t͡ʂtɛrɨ/ was often realized as *sztere* /ʂtɛrɛ/ or *szteri* /ʂtɛrɨ/, with /t͡ʂ/ replaced by /ʂ/. This error was most common among Dutch speakers (9) and was not observed at all in the English group. An interesting case worth mentioning, although it ranks only thirteenth most frequent error, is the tendency of Italian learners to replace the nasal vowel /ɔ̃w̃/ in *niską* /ɲiskɔ̃w̃/ with the sequence /ɔn/, producing forms such as *niskon*. This substitution illustrates the difficulty of acquiring nasal vowels, which are absent from many learners' native phonological systems.

Taken together, these errors point to systematic challenges with Polish retroflex consonants and nasal vowels, as learners tend to replace them with more familiar alveolar sounds or denasalized vowels from their native phonological inventories. The full dataset provides a rich basis for further phonological and cross-linguistic analysis.

#### Visualisation tool

As reading data directly from the raw tables can be somewhat unclear, an interactive HTML platform was developed to facilitate the analysis of learners' pronunciation deviations. This tool allows users to filter all identical correct--erroneous phoneme pairs across the corpus, providing a clear overview of recurring patterns. Additionally, the interface includes buttons for switching between standard IPA representations, offering flexibility depending on the focus of the analysis. The platform serves as a valuable resource for further examining tendencies in Polish interlanguage among learners from the aforementioned countries. Moreover, it enables more detailed investigations into how specific characteristics of learners' native languages may contribute to disfluencies and other systematic deviations.



### Conclusions

From the analysis of both declension and pronunciation errors, several important conclusions can be drawn.

Firstly, with respect to declension, learners tend to overuse the nominative case, which functions as the default or \"base\" form in Polish. In the absence of explicit grammatical knowledge, this case is often overgeneralized to contexts where other forms are required. The results also demonstrate frequent confusion between the genitive, instrumental, locative, and accusative cases, largely due to their morphologically similar suffixes. Such overlap makes them particularly challenging to acquire. Importantly, the analysis suggests that case-related errors are not strongly dependent on the learners' native language (at least within the five examined groups). Instead, they reflect universal developmental patterns and the inherent complexity of the Polish case system. Regarding pronunciation, the errors indicate systematic challenges with Polish retroflex consonants and nasal vowels. While the specific realizations vary across learners' native languages, clear tendencies can be observed for different language groups, suggesting that learners often substitute unfamiliar Polish sounds with more familiar ones from their L1. The patterns observed in the full dataset available through the visualization platform can be used to conduct a more detailed examination of pronunciation deviations, which in turn may facilitate a more effective adaptation of Whisper for accurate interlanguage transcription across different learner groups.

## Evaluation of Whisper's Performance 

### Introduction

This chapter evaluates Whisper's performance in transcribing Polish interlanguage, focusing on its ability to faithfully reproduce learners' speech, including errors and non-standard forms. The analysis highlights the challenges posed by interlanguage, including pronunciation deviations and grammatical errors, and provides insights into the model's strengths and limitations in this context.

### Global Performance

In this section, we assess how Whisper performs when transcribing Polish interlanguage, focusing on its ability to accurately render learner speech at both the word and character levels. To this end, we calculate and analyse two standard ASR evaluation metrics: Word Error Rate (WER) and Character Error Rate (CER). Both metrics are commonly used to quantify ASR performance [@elayari:hal-04769687]. They are based on the Levenshtein distance, which counts the number of substitutions (S), deletions (D), and insertions (I) needed to transform the system output into the reference transcription. Formally, they are defined as follows:





The comparison is based on the full dataset, using the JSON file containing all organised transcriptions for each learner. Given the deformed and often unstable nature of interlanguage, characterised by pronunciation deviations and non-standard forms, relatively low transcription accuracy is to be expected. The same evaluation was also performed on a small corpus of native Polish speech, providing a baseline to compare interlanguage and standard Polish transcription performance.

It is important to note that WER tends to be a weaker metric than CER for the evaluation of interlanguage. As [@wrro207725] point out, WER does not correlate well with human intelligibility, since it ignores semantics, pragmatics, grammar, and other functional aspects of language. In the case of learner speech, this issue is even more pronounced: deviations, particularly those related to pronunciation, often cause entire words to be misrecognised, which heavily penalises the ASR system at the word level. By contrast, CER provides a more fine-grained perspective, as even partially correct transcriptions are rewarded for character-level similarity. Consequently, CER better reflects the degree to which the ASR output preserves traces of the learner's original production, making it a more informative measure in the context of multilingualism [@k2024advocatingcharactererrorrate].

#### WER and CER Results

::: 
  **Metric**            **Score**  
  -------------------- ----------- --
  WER mean                0.754    
  WER median              0.500    
  CER mean                0.464    
  CER median              0.222    
  WER mean (natives)      0.137    
  CER mean (natives)      0.064    

  : Global statistics for WER (Word Error Rate) and CER (Character Error Rate)
:::



The overall results show that Whisper faces significant challenges when transcribing Polish interlanguage. The average WER reaches 75.4%, while the CER of 46.4% reflects frequent inaccuracies at both the word and character level. As expected, the lower CER compared to WER reflects partially correct words that preserve some letters, capturing mostly phonetic approximations typical of interlanguage speech.

A major challenge is the presence of spikes or hallucinated outputs, where Whisper produces incorrect words or phrases, often influenced by strong accents or code-switching. Country-specific performance varies: Italian and British learners showed the highest CERs (above 60%), while Dutch learners achieved the lowest (27%), likely due to clearer articulation.

Consequently, to mitigate the effect of extreme errors, median scores were computed: median WER is 50%, and median CER ranges is 22.2%.

In contrast, evaluation on the small corpus of native Polish speech revealed substantially lower error rates, with a WER of 13.74% and a CER of 6.44%. According to [@elayari:hal-04769687], a WER between 10% and 20% is considered good, indicating that Whisper can reliably transcribe native Polish utterances. The stark difference between the learner and native corpora clearly illustrates the impact of interlanguage on Whisper's performance, highlighting the additional challenges posed by non-native pronunciation, variable articulation, and learner-specific speech patterns.

### Evaluation on Polish Interlanguage

#### Introduction

Since systems like Whisper are trained primarily on standard language transcribing interlanguage presents a significant challenge. This study explores the use of automatic transcription for interlanguage in the context of second language acquisition. In this setting, the goal of the ASR tool is not simply to provide a correct transcription, but rather to reproduce the learner's utterance as faithfully as possible, including any linguistic errors. Overcorrection, therefore, is undesirable, as it obscures the learner's original production. Based on these considerations, it can be hypothesized that overcorrection is likely to be the most frequent type of transcription error encountered in this corpus. In this section, we assess Whisper's performance on such dataset and examine the extent to which its output faithfully reflects the learners' original speech.

#### Evaluation on Pronunciation-Related Interlanguage

##### Corpus Processing

To evaluate Whisper's performance on learner interlanguage phenomena arising from pronunciation-related non-standard forms, a dedicated subcorpus was extracted from the JSON file containing all organized transcriptions. In order to isolate interlanguage forms, the script processed only the manual transcriptions and, based on a Polish lexicon [@polish-nlp-resources], identified word forms that do not appear in the lexicon -- i.e., forms not attested in standard Polish. Unlike the corpus used for the previous statistical error analysis (which consolidated identical errors into aggregated counts and ensured that multiple occurrences of the same error by the same learner were counted only once) this dataset preserves each instance as a separate entry. This format allows for the sequential examination of all occurrences, acknowledging that the corresponding automatic transcriptions produced by Whisper may differ from case to case. Each entry includes relevant metadata such as the learner's country and identification number.

The next step consisted of manually aligning the non-standard forms with both the corresponding automatic transcriptions generated by Whisper and the correct Polish word forms taken from the \"correct version\" segments. Given the nature of the corpus (characterised by frequent deviations) fully automated alignment would likely have yielded very low accuracy. The data was arranged in columns presenting, for each segment, the complete automatic transcription, the manual transcription, and the correct Polish version. Thanks to contextual information, this structure enabled more accurate alignment of individual word forms.

In order to distinguish the nature of the errors and keep only those related to pronunciation, two additional columns were introduced: *declension error* and *pronunciation error*. Each non-standard form underwent automatic verification against two reference datasets -- one listing known declension deviations, and the other containing documented pronunciation deviations from the existing error corpus. If a match was found in either list, the relevant column was marked with *yes*. These automatically assigned labels were then manually verified and, where necessary, corrected to ensure full accuracy. The vast majority of entries in this subcorpus were associated with pronunciation issues, which is unsurprising given that such errors are more likely to produce word forms absent from the lexicon. All examples unrelated to pronunciation were excluded from the dataset.

The final subset comprises 662 non-standard word forms.

::: 
   **Country**   **Learner**  **Interlanguage word**   **Automatic word**   **Correct Polish word**
  ------------- ------------- ------------------------ -------------------- -------------------------
       FR           1120      ulisa                    ulica                ulicą
       FR           1120      ospital                  szpitala             szpitala
       FR           1120      skroczie                 skroczyć             skręcić
       FR           1120      grawo                    prawo                prawo
       FR           1120      piese                    pieśń                pierwszą

  : Excerpt of learner interlanguage words, automatic transcriptions, and correct Polish forms
:::

The script uses the organised subcorpus to analyse how Whisper handled each of these interlanguage forms. For each entry, the tool compared the interlanguage word to the word output by Whisper. The cases were categorized as follows:

-   **Identical reproduction:** the learner's interlanguage word was transcribed exactly as pronounced.

-   **Overcorrection -- correct in the context:** the transcription produces a valid Polish word that fits the intended meaning in the given context.

-   **Overcorrection -- incorrect in the context:** the transcription outputs a valid Polish word, but one that does not match the intended meaning in context.

-   **Hallucination -- word \"invented\" by Whisper:** the model produced invented sequences not found in either the learner's input or the Polish lexicon.

-   **Omission:** the learner's interlanguage form was not transcribed at all.

##### Results

::: 
  **Category**                                                          **Number of words**   **Percentage of corpus**
  ------------------------------------------------------------------- --------------------- --------------------------
  Identically transcribed words                                                          72                     10.88%
  Overcorrected words (correct in context)                                              202                     30.51%
  Overcorrected words (existing in Polish but incorrect in context)                     176                     26.59%
  Words invented by Whisper                                                             108                     16.31%
  Untranscribed words                                                                   104                     15.71%
  **Total**                                                                             662                       100%

  : Distribution of interlanguage words by categories (pronunciation-related errors)
:::



Within this interlanguage subset, 72 words (10.88%) were transcribed identically by Whisper, showing complete overlap between the learner's pronunciation and the model's output. Although this represents a relatively small proportion of the data, it suggests that adapting Whisper for interlanguage transcription may be feasible. As expected, the majority of words (57.1%) were overcorrected. In 202 cases (30.51%), Whisper replaced the interlanguage form with a standard Polish word that was correct in the given context, whereas in 176 cases (26.59%) the substitution was contextually inappropriate, despite the word being valid in Polish. This tendency indicates that, when processing Polish interlanguage, Whisper often normalizes non-standard learner forms into standard Polish rather than reproducing them faithfully. The model also produced entirely new words in 108 cases (16.31%), generating sequences absent from both the original utterance and the Polish lexicon. This behaviour reflects Whisper's inclination to produce plausible-sounding vocabulary when confronted with highly deformed or unclear learner speech. Finally, in 104 instances (15.71%), no transcription was produced at all, a result which nonetheless accounts for a substantial share of the dataset and points to persistent recognition difficulties with certain types of interlanguage input.

#### Evaluation on Declension-Related Interlanguage

##### Corpus Processing

To assess Whisper's ability to process learner interlanguage features stemming from declension errors, a corresponding subcorpus was compiled using data from an error CSV file containing manual transcriptions and their correct versions, alongside a JSON file with organized transcriptions providing the automatic transcriptions. The script filtered the data to include only nouns and adjectives, which are pertinent to grammatical case analysis.

For each instance, pairs of the learner's non-standard forms and the correct Polish counterpart were extracted, accompanied by metadata such as learner ID and country. These entries were further enriched with grammatical case annotations derived from previously curated and manually refined error datasets, ensuring precise labeling of both interlanguage and correct forms.

Consistent with the format adopted for the pronunciation error subcorpus, the data was organized into columns displaying the complete automatic transcription, manual transcription, and the corresponding correct Polish version for each utterance segment. Manual alignment of automatic transcription words to their respective entries was performed to enable detailed analysis.

An automatic morphosyntactic tagging procedure was then applied to assign grammatical case labels to words in the automatic transcriptions. When a word was found in either the interlanguage or correct form dictionaries, the corresponding case was assigned. If absent from both, the Polish *spaCy* model was employed to predict the case. Entries for which automatic tagging failed were flagged for manual review and correction. Among 697 lexical items, 59 cases were automatically identified by *spaCy*, and 15 entries were marked for manual completion.

Following manual corrections, all instances where the interlanguage and correct cases matched (indicating no actual declension error) were excluded from the final dataset. The resulting refined corpus thus contains exclusively authentic grammatical case errors made by learners, providing a solid basis for evaluating Whisper's performance on declension-related interlanguage phenomena. The final file consists of 525 entries.

As in the previous subcorpus dedicated to pronunciation-related errors, this dataset preserves each individual instance separately rather than aggregating identical errors. This approach enables a detailed, sequential analysis of all occurrences, taking into account that Whisper's automatic transcriptions may vary between cases.

::: 
  **Country**   **Learner**   **Word (Interlanguage)**   **Case (Interlanguage)**   **Word (Correct Polish)**   **Correct Case**   **Word (Automatic)**   **Case (Automatic)**
  ------------- ------------- -------------------------- -------------------------- --------------------------- ------------------ ---------------------- ----------------------
  FR            1101          ulica                      Nom                        ulicą                       Ins                ulicę                  Acc
  FR            1101          niska                      Nom                        niską                       Ins                niską                  Ins
  FR            1101          ulica                      Nom                        ulicę                       Acc                ulicę                  Acc
  FR            1101          szpitalu                   Loc                        szpitala                    Gen                szpitala               Gen
  FR            1101          ulic                       ?                          ulicy                       Loc                --                     --

  : Comparison of learner interlanguage, correct Polish forms, and automatic transcriptions with grammatical cases
:::

The script categorizes the types of outcomes produced by Whisper when processing declension-related interlanguage phenomena, as follows:

-   **Faithful reproduction:** Whisper repeats the form used by the learner, reproducing the error.

-   **Overcorrection:** Whisper corrects the learner's form by using the grammatically correct Polish form according to standard grammar rules.

-   **Untranscribed:** Whisper fails to assign any grammatical case or produce a form (missing transcription).

-   **Unknown:** The grammatical case is either unidentified or uncertain, indicated by question marks (\"?\").

-   **Invented form:** Whisper produces a grammatical form different from both the learner's and the correct form.

##### Results

::: 
  **Category**                                         **Number of examples**   **Percentage of corpus**
  --------------------------------------------------- ------------------------ --------------------------
  Faithful reproduction (reproduction of the error)             221                      42.10%
  Overcorrection                                                114                      21.71%
  Not transcribed                                                43                      8.19%
  Unknown                                                        39                      7.43%
  Invented form                                                 108                      20.57%
  **Total**                                                     525                       100%

  : Distribution of interlanguage words by categories (declination-related errors)
:::



The results show that in 42.10% of cases, Whisper faithfully reproduced learners' error, indicating that the system was able to capture the incorrect form as produced. This proportion is notably higher than that observed in the pronunciation error data (10.88%). Invented forms, where Whisper produced a grammatical form different from both the learner's and the correct form, accounted for 20.57% of the dataset. Overcorrections were observed in 21.71% of examples, where the system replaced the learner's form with a different, correct form, potentially masking the learner's actual interlanguage pattern. Not transcribed items represented 8.19%, reflecting instances where the system failed to recognize any input, while in 7.43% of cases the output was ambiguous or unidentifiable.

### Conclusions

The analyses of Whisper's performance on Polish interlanguage highlight distinct tendencies depending on the type of learner errors. For pronunciation errors, the system often overcorrects learner speech, reproducing canonical forms rather than the actual interlanguage output. In contrast, for declension errors, Whisper more frequently reproduces the learner's forms faithfully. However, even the 42% rate of faithful reproduction is still insufficient, indicating that improvements are needed to better capture case-related deviations.

These patterns suggest that Whisper's current architecture is more suited to detecting systematic grammatical errors than phonetic inaccuracies. However, in the context of automatic transcription of interlanguage, this implies that while Whisper can provide a foundation for monitoring learner productions, enhancing the model's sensitivity to both pronunciation and declension deviations would make it a more effective tool for accurately capturing interlanguage phenomena.

## Future Perspectives 

### Introduction

One promising direction for improving Whisper's performance on learner speech is the development of a version adapted specifically to Polish interlanguage. This could potentially be achieved through fine-tuning the model using a dedicated interlanguage corpus. In such a setup, the system would be trained to recognize and transcribe interlanguage forms, rather than correcting them into standard Polish. The new vocabulary -- reflecting common learner errors -- would help the model predict and output words closer to what the learner actually said. However, to ensure high data quality and reliability, the interlanguage dataset used for fine-tuning would need to be manually annotated by native Polish speakers, ideally with a background in linguistics or second language acquisition.

### Open Questions and Obstacles

A key question in designing such a system is whether it should be tailored to learners of a specific native language or whether a more general model would suffice. On the one hand, the error analysis in this study shows that speakers of different native languages often exhibit consistent patterns, particularly in pronunciation. This suggests that separate models for pronunciation errors could be developed for different L1 groups, although some errors may also be universal across learners. On the other hand, case-related errors appear to be largely independent of the learner's native language, indicating that a universal model would likely be sufficient for handling morphological deviations.

A major challenge remains the inherently dynamic and individual nature of interlanguage. Learners follow unique developmental trajectories, and errors evolve over time depending on exposure, proficiency, and learning strategies. This raises questions about whether separate corpora or models would be needed for different proficiency levels, which would significantly increase data requirements and necessitate careful learner selection.

Finally, the corpus used in this study is highly task-specific, focusing exclusively on giving and understanding route directions. To develop a more robust and generalizable interlanguage-adapted Whisper, training data would need to cover a broader variety of linguistic contexts and speaking styles, including both spontaneous and scripted speech across different communicative situations.

Another avenue for future development is the creation of a dual-model system for language learning. One model could faithfully reproduce the learner's interlanguage, showing exactly what the learner said, while a second model could provide the corrected, standard version of the utterance. Such a setup would allow learners to compare their own productions with the target forms, supporting both self-monitoring and guided correction.

Moreover, for case-related learning, tools such as *spaCy* could be employed to automatically identify cases in learner speech. However, current results indicate that *spaCy* does not yet handle this task with high accuracy, highlighting an area for potential improvement in future work.

## General conclusion 

The present study has investigated the acquisition of Polish as a foreign language by adult learners within the framework of the VILLA project, focusing in particular on oral production data collected from the Route Direction task. By combining manual transcriptions with automatic speech recognition with Whisper, the research has offered both a qualitative and quantitative perspective on learner errors, with special attention to the influence of the native language and the challenges posed by the phonological and morphological systems of Polish.

The analysis has highlighted that interlanguage remains a dynamic and systematic system shaped by a variety of factors, including but not limited to the learners' mother tongue. While some transfer from the native language was likely, particularly in pronunciation-related cases, the results also showed that learners employed strategies such as simplification, overgeneralization, or omission, confirming the multifaceted nature of early second language acquisition. The frequent occurrence of errors related to pronunciation and case marking further underlines the intrinsic complexity of Polish for non-Slavic learners, especially after such limited exposure.

At the methodological level, the study has shown the relevance of combining manual annotation with automatic tools. Although automatic speech recognition systems like Whisper are not flawless in handling learner data, they provide a useful starting point for analysis and open perspectives for future applications in second language research and pedagogy.

Overall, the findings of this work contribute to a better understanding of the processes involved in the earliest stages of second language acquisition. They emphasize the importance of taking into account both cross-linguistic influences and the structural characteristics of the target language when developing tools for the automatic transcription of interlanguage. Furthermore, the integration of computational tools into corpus-based research holds promise for more efficient and large-scale analyses of learner data.

## Documentation

### Example XML File 

::: center
    <annotations>
    <apprenant_id>1108</apprenant_id>
    <pays>FR</pays>
    <enonce id="1">
    <STU>
    dobrej cztery proszę idź prosto ulika niska prosto prosto
    </STU>
    <POL>
    do dobrej cztery proszę iść prosto ulicą niską prosto prosto
    </POL>
    </enonce>
    <enonce id="2">
    <STU>
    szken szken szkensiś na prawo ulica dżoliesa slołackiego
    </STU>
    <POL>skręcić w prawo w ulicę juliusza słowackiego</POL>
    </enonce>
    <enonce id="3">
    <STU>idź prosto</STU>
    <POL>idź prosto</POL>
    </enonce>
    <enonce id="4">
    <STU>obok skola obok uniwersitet</STU>
    <POL>obok szkoły obok uniwersytetu</POL>
    </enonce>
    <enonce id="5">
    <STU>proszę idź prosto</STU>
    <POL>proszę idź prosto</POL>
    </enonce>
    <enonce id="6">
    <STU>i ulika dobra skręcisz na lewo</STU>
    <POL>i w ulicę dobrą skręcisz w lewo</POL>
    </enonce>
    <enonce id="7">
    <STU>najduje się dom kowalska </STU>
    <POL>znajduje się dom kowalskich</POL>
    </enonce>
    </annotations>
:::

### Fragment of the JSON file containing organised transcriptions and correct Polish versions 

::: adjustbox
angle=90, max width=

    [
        {
            "numéro d'apprenant": "1114",
            "pays": "FR",
            "transcription_automatique_non_pl": "we are at the railway station i am a tourist from warsaw (...)",
            "transcription manuelle (1)": "proszę idź na ulicza niska",
            "version correcte en polonais (1)": "proszę iść ulicą niską",
            "transcription manuelle (2)": "strejć prawo na ulicza juliuska słowackiego",
            "version correcte en polonais (2)": "skręć w prawo w ulicę juliusza słowackiego",
            "transcription manuelle (3)": "proszę idź proszę idź strejć lewo na ulicza dobra",
            "version correcte en polonais (3)": "proszę iść proszę iść skręć w lewo w ulicę dobrą",
            "transcription manuelle (4)": "znajdywo się la kowalski dom dom kowalski",
            "version correcte en polonais (4)": "tam znajduje się dom kowalskich"
        },
        {
            "numéro d'apprenant": "1120",
            "pays": "FR",
            "transcription automatique": "tak po prostu ulica niska obok szpitala po prostu skroczyć na na prawo pieśń (...)",
            "transcription manuelle (1)": "tak prosto ulisa niska obok ospital",
            "version correcte en polonais (1)": "tak prosto ulicą niską obok szpitala",
            "transcription manuelle (2)": "prosto i skroczie na na grawo piese ulisa skrecić na prawo ulisa żuliesa",
            "version correcte en polonais (2)": "prosto i skręcić w prawo w pierwszą ulicę skręcić w prawo w ulicę juliusza",
            "transcription manuelle (3)": "i pies pro proto proto ubak ubok restorancja ubok teatr i ubok skola juwersytet",
            "version correcte en polonais (3)": "potem prosto prosto obok restauracji obok teatru obok szkoły uniwersytetu",
            "transcription manuelle (4)": "i skroczie na lewo ulisa dobra pies prosto (...)",
            "version correcte en polonais (4)": "i skręcić w lewo w ulicę dobrą proszę prosto i skręcić w lewo w ulicę (...)",
            "transcription manuelle (5)": "jest na lewo",
            "version correcte en polonais (5)": "jest na lewo"
        }
    ]
:::

### Example of a group of words associated with the same lemma 

        "sklep": [
            "szklep",
            "skelp",
            "sklepiem",
            "spren",
            "sklep",
            "sklept",
            "skret",
            "skre",
            "szklebo",
            "helen",
            "sklepem",
            "slepu",
            "salsklepu",
            "szklapu",
            "szlep",
            "sklepu",
            "sken",
            "szklepem",
            "sklepe",
            "sklepd",
            "skaczie",
            "sklepen",
            "sklepie",
            "sklepts",
            "szklebu",
            "szklepu",
            "skren",
            "szkleb",
            "szklepe",
            "sklebe"
        ],

### Example of a segment with pairs of words from the manual transcription and the corresponding correct version 

::: center
    [
        {
            "apprenant": "1114",
            "pays": "FR",
            "segments": [
                {
                    "segment_id": 1,
                    "segments": [
                        {
                            "manuel": "proszę",
                            "correct": "proszę"
                        },
                        {
                            "manuel": "idź",
                            "correct": "iść"
                        },
                        {
                            "manuel": "na",
                            "correct": "-"
                        },
                        {
                            "manuel": "ulicza",
                            "correct": "ulicą"
                        },
                        {
                            "manuel": "niska",
                            "correct": "niską"
                        }
                    ]
                },
:::

: <https://pl.wikipedia.org/wiki/Alfabet_polski>

: IPA transcriptions were generated using the online converter: <https://baltoslav.eu/ipa/index.php?mova=pl>

: Whisper: <https://github.com/openai/whisper>

: Huma-Num: <https://documentation.huma-num.fr/sharedocs-stockage/>

: spaCy: <https://spacy.io/>

: Pandas: <https://pandas.pydata.org/>

: Fuzzywuzzy: <https://pypi.org/project/fuzzywuzzy/>

: Epitran: <https://pypi.org/project/epitran/>

: Langdetect: <https://pypi.org/project/langdetect/>

: Matplotlib: <https://matplotlib.org/>

: Seaborn: <https://seaborn.pydata.org/>

: JiWER: <https://pypi.org/project/jiwer/>
