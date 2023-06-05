
#GY prompts

# This prompt provides the context for the summarization of the non-negative matrix factorizations
prompt = """
You will act as an explainability module, providing a narrative explanation of what types of content clusters of artificial neurons are selectively attending to.
You will receive text consisting of: 
Some text initially given as input to some large language model.
This text might be natural language or code written in some programming language.
Several versions of the initial text given as input, mentioned above, but with some tokens replaced by an underscore: "_".
The tokens, which have not been replaced by an underscore, has been shown to be activated by some cluster of neurons of the large language model, in response to the input shown earlier.
These clusters have been found through non-negative matrix factorization.
Your job is to describe any relationship which might be present between the tokens, which are not replaced by underscores.
These relationships might be syntactic, grammatic, semantic or some special token of the large language model like "[CLS]" and "[SEP]".
Or they might just be selectively attending to particular pieces of a sentence like the start, middle or the end.
There can also be many more ways, not explicitly mentioned above, in which the tokens might be related.
It is your job to try to describe these relationships to the best of your ability.
The activity of the neurons, which have clustered in response to certain portions of the output are selected using some threshold. 
This technique is not perfect!
For this reason, there might be some tokens which don't seem to be connected to the rest of the tokens, even if they are not blanked out.
You are allowed to summarize the general tendencies of the tokens which have not been blanked out, while skipping a smaller portion of these tokens, if they don't seem to be related to the rest of the tokens.

The response should be moderately brief, unless a longer explanation is absolutely nescessary - like if you left out some tokens that don't seem to make sense in the context of the other tokens.
If there is no clear relationship between any of the tokens, you should add something like: "There seems to little connection between the tokens of this layer: [Insert example of tokens]", to show your uncertainty.
If you are unsure of the relationship between the tokens you must suggest the following:
In order to understand this relationship better, it might help to adjust the threshold used to mask tokens, or the number of components in the non-negative matrix factorization.
In addition the non-negative matrix factorization could be performed on individual layers, or the entire model - either of which might be more informative.

Below I will provide some examples:
Example 1:
"Your input text:
"The original string input was: '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18'. \nThe activations used to mask tokens was found with a threshold of 0.01. \nThe activations were decomposed into 5 factors. \nAny mask is marked by replacing the original text with an underscore: '_' Factor number 1 contained these tokens: '_,2,3,4,5_6_7_8_9_10_11_12,13,_________'. \nFactor number 2 contained these tokens: '_________,_,_,_,_,_,_,_,_,_,_,_,_,_'. \nFactor number 3 contained these tokens: '____3_4_5_6,7_8_9_10_11_12_13_14_15_16_17_18'. \nFactor number 4 contained these tokens: '_,_,_,_,_,_,_,8,_,10,_,_,_,_,_,_____'. \nFactor number 5 contained these tokens: '1__________________________________'. \n"

Explanation output (what you should produce):
"The activations have been composed into 5 factors.
Factor 1 seems to selectively respond to the numbers in the middle of the sequence.
Factor 2 seems to selectively respond to the commas near the middle to the end of the sequence.
Factor 3 seems to selectively respond to the numbers throughout the sequence - only skipping the first numbers.
Factor 4 seems to selectively respond to the commas in the early and middle part of of the sequence.
Factor 5 seems to selectively respond to the very first token in the sequence and nothing else.
In summary some tendencies can be observed in these factors, with factors responding selectively based on the position in the input sequence (like factor 1, 4 and 5) and based on the content of the token (some factors responding selectively to commas (factor 2) and others to numbers (factor 3))."

Example 2:
"Your input text:
'The original string input was: \'Ċ<page>ĊĠ<title>Antichrist</title>ĊĠ<id>865</id>ĊĠ<revision>ĊĠĠĠ<id>15900676</id>ĊĠĠĠ<timestamp>2002-08-03T18:14:12Z</timestamp>ĊĠĠĠ<contributor>ĊĠĠĠĠĠ<username>Paris</username>ĊĠĠĠĠĠ<id>23</id>ĊĠĠĠ</contributor>ĊĠĠĠ<minor/>ĊĠĠĠ<comment>Automatedconversion</comment>ĊĠĠĠ<textxml:space="preserve">#REDIRECT[[Christianity]]</text>ĊĠ</revision>Ċ</page>Ċ\'. \nThe activations used to mask tokens was found with a threshold of 0.01. \nThe activations were decomposed into 10 factors. \nAny mask is marked by replacing the original text with an underscore: \'_\' Factor number 1 contained these tokens: \'____Ċ______</________</_______Ċ________</__________-_-_____:__</timestamp__________________</username__________</id__ĠĠĠ</contribut________/>__________</comment______xml__="__">#___[[__]]</text__Ġ</re___</___\'. \nFactor number 2 contained these tokens: \'______title_____title>ĊĠ<id___</id>Ċ__vision_____id__900676</id>Ċ_ĠĠ<_estamp_2002_08_03_____12Z_timestamp>__Ġ___or_____Ġ_username__</username>ĊĠĠĠĠ_id__</id>ĊĠĠ_contributor>_____or__ĠĠĠ<comment__ated_version_comment>_ĠĠĠ<text_____erve____RECT__ity__text>__revision>__page>_\'. \nFactor number 3 contained these tokens: \'_<_>___>Antichrist__>__id>865_id____vision>_ĠĠ___15900676____Ġ__timestamp_2002-08_03_18_14_12Z_timestamp__Ġ___ributor>ĊĠ____username_Paris_username_Ċ_______23______Ġ</_ributor_ĊĠ__minor/>ĊĠ__comment>Automatedconversion</__Ċ____xml:space="preserve">#REDIRECT[[Christianity]]____Ġ</_vision_Ċ</___\'. \nFactor number 4 contained these tokens: \'_<__ĊĠ<___ich_</___Ġ<id>8__id__Ġ<re_>_Ġ_Ġ<id>_________Ġ<__>_-_-_______________Ġ<___>Ċ_ĠĠ_Ġ<_>_</_______Ġ<id>23______Ġ</_____ĠĠĠ<minor____Ġ<_>_ated________Ġ<text_:_="__">#___[[___</___Ġ</re___</___\'. \nFactor number 5 contained these tokens: \'_<page>__title>__rist_title>___>865__>____>_____>15900676__>_____estamp>_-_________Z</__>______or>______username>___>Ċ____Ġ<_>___>Ċ_____or>ĊĠĠĠ<_or/>Ċ__Ġ<_>_ated_version</_>Ċ__Ġ<_xml:_="_erve">#___[[__]]__>Ċ__vision>Ċ</page>Ċ\'. \nFactor number 6 contained these tokens: \'_<page>_Ġ<title____</title___id________revision____Ġ<id___________timestamp_____03T__14_12Z_tim___Ġ__contributor__ĠĠĠ__username___username_______id________Ġ</contributor_____minor/>____comment_Autom_conversion_comment_____textxml:space="preserve">#REDIRECT_Christian_]]</text_ĊĠ</revision___page_Ċ\'. \nFactor number 7 contained these tokens: \'_<______Ant_______id_8___>______ĠĠĠ<id_15900__id>ĊĠĠĠ<tim__2002___03______Z</tim_>ĊĠĠĠ<cont__>_ĠĠĠĠĠ<username_Paris__>ĊĠĠĠĠ_id_23</_>ĊĠĠ_cont_or>ĊĠĠĠ<min_/>ĊĠĠĠ<comment_Autom_con_</_>ĊĠĠĠ<__:_____#_________>Ċ_re_>Ċ__>_\'. \nFactor number 8 contained these tokens: \'____Ċ_________ĊĠ<_______Ċ____Ċ________</_>Ċ_______-_-___:_:______Ċ_______Ċ_________username_ĊĠĠĠ_____</_>ĊĠĠ___or>Ċ______ĊĠĠ_________>ĊĠĠ___:_="__">#___[[__]]_text>ĊĠ</revision>Ċ</page>Ċ\'. \nFactor number 9 contained these tokens: \'_________________>865_id>ĊĠ<re_>Ċ__Ġ<_>15900676</id_ĊĠĠĠ<timestamp>2002-08-03T18:14:12Z</timestamp>ĊĠĠĠ<cont___Ċ______>Paris_username________>23_____________________________________:space="___#_I__________________\'. \nFactor number 10 contained these tokens: \'Ċ<__Ċ__>_________>_______________>______________-_-____________________Ċ______>___________>__________________________ated______________________________________\'. \n'

The output explanation (which you should produce):
Factor 1 seems to selectively respond to the "less-than" symbol "<" which is used in the start XML tags.
Factor 2 and 6 both seem to selectively respond to the tags of the xml, contained between a "<" (less-than symbol) and a ">" (larger than symbol).
Factor 3 seems to selectively respond to the text inside the xml tags.
Factor 4 seems to selectively respond to the token for spaces and indentation: "Ġ", but only when these are immediately followed by the less-than symbol "<" which is used in the start of XMl tags.
Factor 5 seems to selectively respond to the "greater-than" symbol ">" which is used in the end of XML tags.
Factor 7 seems to selectively respond to line-breaks, denoted by the "Ċ" token.
Factor 8 seems to selectively respond to indentations denoted by the "Ġ" token.
Factor 9 seems to selectively respond to sequences of numbers.
Factor 10 seems to be selectively responding to the very first token and nothing else.
In summary, these factors very syntax-sensitive (like factor 1, 2, 3, 4, 5, 6, 7, 8), since all these factors are responding to some symbol denoting the syntax.
Some other factors are responding selectively to certain positions of the input like the start (factor 10) and the content of numbers (factor 9)"

Follow the advice and examples as closely as possible for the following input text:
"""


#Example 2:
#Your input text:
#"The original string input was: '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18'. \nThe activations used to mask tokens was found with a threshold of 0.01. \nThe activations were decomposed into 5 factors. \nAny mask is marked by replacing the original text with an underscore: '_' Factor number 1 contained these tokens: '_,2,3,4,5_6_7_8_9_10_11_12,13,_________'. \nFactor number 2 contained these tokens: '_________,_,_,_,_,_,_,_,_,_,_,_,_,_'. \nFactor number 3 contained these tokens: '____3_4_5_6,7_8_9_10_11_12_13_14_15_16_17_18'. \nFactor number 4 contained these tokens: '_,_,_,_,_,_,_,8,_,10,_,_,_,_,_,_____'. \nFactor number 5 contained these tokens: '1__________________________________'. \n"
#
#Explanation output (what you should produce):
#"The activations have been composed into 5 factors.
#Factor 1 seems to selectively respond to the numbers in the middle of the sequence.
#Factor 2 seems to selectively respond to the commas near the middle to the end of the sequence.
#Factor 3 seems to selectively respond to the numbers throughout the sequence - only skipping the first numbers.
#Factor 4 seems to selectively respond to the commas in the early and middle part of of the sequence.
#Factor 5 seems to selectively respond to the very first token in the sequence and nothing else.
#In summary some tendencies can be observed in these factors, with factors responding selectively based on the position in the input sequence (like factor 1, 4 and 5) and based on the content of the token (some factors responding selectively to commas (factor 2) and others to numbers (factor 3))."

#Example 2:
#"Your input text:
#'The original string input was: \'TheĠcountriesĠofĠtheĠEuropeanĠUnionĠare:Ċ1.AustriaĊ2.BelgiumĊ3.BulgariaĊ4.CroatiaĊ5.CyprusĊ6.CzechRepublicĊ7.Denmark"Ċ\'. \nThe activations used to mask tokens was found with a threshold of 0.01. \nThe activations were decomposed into 6 factors. \nAny mask is marked by replacing the original text with an underscore: \'_\' Factor number 1 contained these tokens: \'__ĠofĠtheĠEuropean______Aust____Belg____Bulgar____Croat____Cyprus___CzechRepublic___Den___\'. \nFactor number 2 contained these tokens: \'___Ġthe__Ġare_Ċ____Ċ_____Ċ_____Ċ_____Ċ_.__Ċ_.__RepublicĊ_.__"Ċ\'. \nFactor number 3 contained these tokens: \'__ĠofĠthe__Ġare:Ċ1.__Ċ2____Ċ3_____4_____5____6_C___7___"_\'. \nFactor number 4 contained these tokens: \'__ĠofĠthe__Ġare:Ċ1.__Ċ_.Bel__Ċ_._____._____.____.C____.__"_\'. \nFactor number 5 contained these tokens: \'TheĠcountriesĠofĠthe__Ġare:Ċ_.____________________________________"_\'. \nFactor number 6 contained these tokens: \'_ĠcountriesĠofĠtheĠEuropeanĠUnionĠare:Ċ1.AustriaĊ2._giumĊ___garia____atia____prus____zechRepublic___Denmark"_\'. \n'
#
#The output explanation (which you should produce):
#Factor 1 seems to selectively respond to geographical locations in the input prompt: The european union, Austra, Belgium, Bulgaria, etc.
#Factor 2 seems to selectively respond to the symbol Ċ, which corresponds to the token for line-changes linebreaks.
#Factor 3 seems to selectively respond to the sequence of numbers 1 to 7, used in listing the countries.
#Factor 4 seems to selectively respond to the period following each number, denoting the sequence/listing of the countries.
#Factor 5 seems to selectively respond to the beginning of the sequence, specifically the first sentence.
#Factor 6 seems to selectively respond to the beginning, as well as the subsequent listing of countries - the exact nature of the relationship between these tokens is less clear.
#Many of the factors, however, also seem to attend partly to the first part of the sentence, as well to the groups described above.
#In summary some factors are quite clear (like factor 1-5), while the relationship between the tokens in factor 6 is less clear.
#The tokens in factor 6 were: '_ĠcountriesĠofĠtheĠEuropeanĠUnionĠare:Ċ1.AustriaĊ2._giumĊ___garia____atia____prus____zechRepublic___Denmark"_\'. \n'
#In order to understand this relationship better, it might help to adjust the threshold used to mask tokens, or the number of components in the non-negative matrix factorization.
#In addition the non-negative matrix factorization could be performed on individual layers, or the entire model - either of which might be more informative."

#Example 1:
#Your input text:
#"The original string input was: '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18'. \nThe activations used to mask tokens was found with a threshold of 0.01. \nThe activations were decomposed into 2 factors. \nAny mask is marked by replacing the original text with an underscore: '_' Factor number 1 contained these tokens: '_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_'. \nFactor number 2 contained these tokens: '1,2,3,4,5,6,7,8,9_10_11_12_13_14_15_16_17_18'. \n"
#
#Explanation output (what you should produce):
#"The activations have been composed into 2 factors.
#Factor number 1 seems to selectively respond to commas.
#Factor number 2 seems to selectively factor to incrementing numbers.
#In summary, these factors correspond well the alternating pattern of commas (factor 1), and incremented numbers (factor 2) given as input to the large language model."