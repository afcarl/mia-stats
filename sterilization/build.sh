pandoc -i bayesian-methods.md \
    -m \
    -o bayesian-methods.docx

git add .
git commit
git push
