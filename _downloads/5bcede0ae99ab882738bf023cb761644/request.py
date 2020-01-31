"""
NeuroSpin file fetcher
======================

Credit: A Grigis

All the returned path are relative as the files are usually on network
resources, and that those resources are mounted in a user-specific location.

In order to test if the 'blizzard' package is installed on your machine,
you can check the package version.
"""

from pprint import pprint
import blizzard
from blizzard import Blizzard
print(blizzard.__version__)

#############################################################################
# Now we create a connection to the ElasticSearch service and display its
# status.

filer = Blizzard(url="https://kratos.intra.cea.fr", verify_certs=False)
info = filer.status()

#############################################################################
# The API provides two methods: 'list' (equivalent to a Linux ls) or 'search'
# (equivalent to a Linux find with predifined search keys). A file path
# is splitted using '_' and '/' to generate search keys.
#
# Working with BIDS datasets
# --------------------------
#
# We start listing all the subjects available in the Localizer dataset.

subjects = filer.list("/localizer/sourcedata")
pprint(subjects)

#############################################################################
# We then list all the anatomical files of a specific subject in session V1.

anatfiles = filer.list("/localizer/sourcedata/sub-S58/ses-V1/anat")
pprint(anatfiles)

#############################################################################
# We do the same using the search interface. It is not mandatory to specify
# the session in the search as there is only one session in this study.

files = filer.search(["localizer", "sourcedata", "sub-S58", "anat"])
pprint(files)

#############################################################################
# Finally we list all the NIFTI T1-weighted MRI images of the study.

files = filer.search(["localizer", "sourcedata", "acq-maskface", "defaceT1w",
                      "niigz"])
print(len(files))
pprint(files[:10])

#############################################################################
# Here we do the exact same but for the UKB study.

subjects = filer.list("/ukb/sourcedata")
pprint(subjects[:10])
anatfiles = filer.list("/ukb/sourcedata/sub-6024431/ses-2/anat")
pprint(anatfiles)
files = filer.search(["ukb", "sourcedata", "sub-6024431", "anat"])
pprint(files)
files = filer.search(["ukb", "sourcedata", "T1w", "niigz"])
print(len(files))

#############################################################################
# If multiple datasets are organized using a common organization (here BIDS)
# its is really easy to make a cross study search.

files = filer.search(["sourcedata", "T1w", "niigz"])
print(len(files))
pprint(files[:10])

#############################################################################
# Working with custom datasets
# ----------------------------
#
# When the dataset is not organized using well documented organization, you
# may start listing the study tree to infer the search keys.
#
# Here is an example for the HCP dataset.

subjects = filer.list("/hcp/PROCESSED/3T_structural_preproc")
pprint(subjects[:10])
anatfiles = filer.list("/hcp/PROCESSED/3T_structural_preproc/894673/T1w")
pprint(anatfiles)
files = filer.search(["hcp", "structural", "preproc", "894673", "T1w"])
print(len(files))
pprint(files[:10])
files = filer.search(["hcp", "structural", "preproc", "T1w", "dc",
                      "brain", "niigz"])
print(len(files))
pprint(files[:10])
