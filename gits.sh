# how to run:
# go to your root acme directory with the volume1 and volume2 sub-directories
# run 

# bash gits.sh "type commit message here"

# Ex: I have Acme/Junior/volume1 and Acme/Junior/volume2 so I would run
# bash gits.sh "commit message" in the Acme/Junior/ directory

if [ $# -eq 0 ]
  then
    echo "No message supplied"
    git add --all
    git commit -m "pushing"
    git pull origin main
    git push origin main
fi

if [ $# -eq 1 ]
  then
    git add --all
    git commit -m "$1"
    git pull origin main
    git push origin main
fi


