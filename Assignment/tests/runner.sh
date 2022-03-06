export PATH=.:$PATH

# compile

cd input
find ./* -maxdepth 1 | xargs -I {} -n 1 bash -c '../tcompiler {} > ../output/{}'

# compare

cd ../output
find ./* -maxdepth 1 | xargs -I {} -n 1 bash -c '
  if diff {} ../expected/{} > /dev/null; then
    printf "\x1b[92mTEST PASSED: {}\x1b[0m\n"
  else
    printf "\x1b[91mTEST FAILED: {}\x1b[0m\n"
  fi
'