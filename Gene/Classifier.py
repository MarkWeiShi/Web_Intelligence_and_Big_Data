#Created by Mark Shi for Web Intelligence and Big Data Coursera Assignment HW7 - Genetic Analytics

import orange
data = orange.ExampleTable("genestrain.tab")
prediction = orange.ExampleTable("genesblind.tab")
classifier = orange.BayesLearner(data)
for i in prediction:
    result = classifier(i)
    print "%s" % (result)
