while read p; do
  echo "$p"
  pip install "$p" || echo "Failed to install $p"
done <requirements.txt
