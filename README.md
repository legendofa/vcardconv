# vcardconv
This repository is inteded for converting vCards from version 2.1 to 4.0 with a python script.

Your mileage may vary depending on which attributes your contacs have.

Example:


| 2.1 | 4.0 |
| - | - |
| BEGIN:VCARD<br>VERSION:2.1<br>N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=52=65=6E;=4B=79=6C=6F;;;<br>FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=4B=79=6C=6F=20=52=65=6E<br>TEL;CELL:'this is a number'<br>BDAY:YYYY-MM-DD<br>EMAIL:kyloren@bar.com | BEGIN:VCARD<br>VERION:4.0<br>N:Ren;Kylo;;;<br>FN:Kylo Ren<br>TEL;CELL:'this is a number'<br>BDAY:YYYY-MM-DD<br>EMAIL:kyloren@bar.com |
