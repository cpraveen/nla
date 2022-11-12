# Download data files from bitbucket
# Run inside DATA directory like this
#     sh ./download.sh

BASEURL=https://bitbucket.org/cpraveen/nla/downloads

FILES="allFaces.mat \
       ovariancancer_obs.csv \
       ovariancancer_grp.csv \
       dog.jpg"

for file in $FILES
do
   echo "----------------------------------------------------------------------"
   echo " Downloading $file"
   echo "----------------------------------------------------------------------"
   wget -c $BASEURL/$file
done
