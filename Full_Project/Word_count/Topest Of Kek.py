sample1 = "Since 2010, Apple has annually announced a new version of iOS and a software developer’s kit." \
                   "Android releases new APIs every half year and a major new version every year. " \
                   "As more and more developers join mobile-software development, the competition heats up. " \
                   "The time to market decreases and could be less than 18 weeks, leaving little time for testing."

sample2 = "Expectations regarding features, time to market, and reliability are placing tremendous strain on software quality processes. " \
          "Software quality assurance costs often dwarf development costs. Testing is a dominant element in software quality assurance." \
          " Manually writing software tests is tedious and difficult and often gives poor coverage of the source code. " \
          "Developers spend much effort improving these manually written test suites, often leading to development cost overruns."

sample3 = "Software today attracts more investment than most other industries." \
" In turn, the market valuation of such innovative “digitized” industries is growing faster, thereby continuously accelerating innovation." \
" This self-amplifying effect requires creative developers who can quickly grow their competences." \
" Because software is flexible and easily changed, many products and releases don’t always create real value." \
" Because production and logistics are of limited relevance and incur only marginal costs, new, innovative players can easily enter a market and sell globally."


import re

regexPat = re.compile(r"(\w*)\b")


trawled1 = regexPat.findall(sample1)
trawled2 = regexPat.findall(sample2)
trawled3 = regexPat.findall(sample3)
#print(trawled2)
def popwhitespace(x):
    """
    jajdjajddi
    :param x: list of a Sample
    :return:
    """
    for i in x:
        if i == '':
            x.pop(x.index(i))

popwhitespace(trawled1)
popwhitespace(trawled2)
popwhitespace(trawled3)
dict1 = dict(trawled1)
print(set(trawled2) & set(trawled1))
#print(trawled2)