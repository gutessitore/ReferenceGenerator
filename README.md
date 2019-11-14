# ReferenceGenerator
python web scrapping program that generate references in the ABNT format.
The name of the site is based on the url, the title from the actual HTML ```<title>``` tag. And the date is randomly generated in between two dates.

---
**Basic output**

EDITOR.MD. Open source online Markdown editor. Disponível em: https://pandao.github.io/editor.md/en.html. Acesso em: 8 nov. 2019.

A pdf file with multiple references following the format above

---
#### Disclaimer
Progam does not work with all links, some sites don't have titles, in this case the output title will be replaced by "Sem título".
###Bugs
- Titles with strange letters cant be reproduced in the pdf output. (can be fixed by adding a new font)
