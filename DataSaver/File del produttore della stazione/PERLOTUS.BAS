1 CLS
10 locate  7,16:input "Numero di misure memorizzate.......................",mis
15 LOCATE 11,16:PRINT "Inizio procedura per conversione file...........(A)"
20 LOCATE 15,16:PRINT "Uscita a sistema operativo MS/DOS...............(B)"
30 A$=INKEY$:IF LEN(A$)=0 THEN 30
31 IF A$="B" THEN SYSTEM
32 IF A$="A" THEN GOTO 40
33 A$="":GOTO 30
40 LOCATE 17,16:INPUT "Nome del file da convertire.............";MAME$
50 LOCATE 19,16:INPUT "Nome del file di uscita.................";NAM$
55 LOCATE 21,16:COLOR 23,0:PRINT "Prego attendere fine elaborazione.......";:COLOR 7,0
60 OPEN "I",#1,MAME$
70 OPEN "O",#2,NAM$
80 IF EOF(1) THEN GOTO 320
90 INPUT #1,A$
100 IF A$="H" THEN GOTO 130
120 GOTO 80
130 PRINT #2,A$+" ";
140 IF EOF(1) THEN GOTO 320
150 INPUT #1,A$:PRINT #2, USING "##.##";VAL(A$);:PRINT #2, " ";
160 IF EOF(1) THEN 320
170 INPUT #1,A$:PRINT #2, USING "##";VAL(A$);
180 IF EOF(1) THEN 320
190 INPUT #1,A$:PRINT #2, "/";:PRINT #2, USING "##";VAL(A$);
200 FOR I=1 TO mis
210 INPUT #1,A$
220 IF A$="S" THEN 240
230 PRINT #2, USING "#####.#";VAL(A$);
240 NEXT I
250 PRINT #2,CHR$(13)
260 GOTO 80
320 CLOSE #1
330 CLOSE #2
340 CLS:GOTO 10
