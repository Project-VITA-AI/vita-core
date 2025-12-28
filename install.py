import nltk

nltk.download("averaged_perceptron_tagger_eng")

from unidic.download import download_version
import plac

plac.call(download_version)
