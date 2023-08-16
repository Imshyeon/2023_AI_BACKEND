cd c:/pywork/img
for file in *.jpg; do
   mongofiles -v -d images -t image/jpeg -r put "$file"
done

//for %i in (c:\pywork\img\*.*) do mongofiles -v -d images put %i