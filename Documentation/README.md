# Tutorial Stazione Meteo ITIS Max Planck - Laboratorio Fisica
Bortot Michele: Le scritte in MAIUSCOLO sono bozze da estendere, mi dispiace se non é completo il file ora come ora

<h3>Come accedere alla raspberry</h3>
<ol>
   <li>
    Avvisa il tuo professore di informatica o sistemi (se non sanno che pesci pigliare rivolgiti a quelli di un'altra sezione).
  </li>
  <li>
    Presentati ai professori di fisica cosí da avere accesso al laboratorio e alla teca quando vuoi.
  </li>
  <li>
    Connettiti con un portatile al rasperry via <a href="http://www.putty.org/">putty (SSH)</a> e <a href="https://www.youtube.com/watch?v=miGXUFyBvJQ">Xming (Grafica)</a>>  o portatelo a casa e collegalo ad un monitor via HDMI
  </li>
    Clona la repository nel tuo git e carica lí i tuoi aggiornamenti
  </li>
  <li> 
    
  </li>
 </ol>
<br>

<h3>Come leggere dati dalla stazione</h3>
   <h4>Windows</h4>
      <ol>
         <li>
            Connetti il connettore usb(adattatore a seriale) al computer.
         </li><li>
            installa un terminale seriale (io ho usato [terminal com] (https://sites.google.com/site/terminalbpp/)) 
         </li><li>
            seleziona la porta giusta e comincia a leggere il flusso
          </li></ol>
   <h4>Raspbian</h4>
      <ol>
         <li>
           Connetti il connettore usb(adattatore a seriale) ad una porta del raspberry.
   </li><li> digita nel terminale <code>dmesg | grep tty</code>
   </li><li> dovresti riceve come risposta <code>[    5.505049] usb 1-1.2: pl2303 converter now attached to ttyUSB0
</code>, ttyUSB0 é la porta dove hai collegato il convertitore usb-seriale.
   </li><li></li>
   </ol>
  <h3>Esemipio di dati</h3>
      <code>
      PROG. N.40 ORE 15 :58 :2 DEL 8 /2 /18 
      SAT. N. 1 
      SONDA N. 1.01: 8.4 GC 
      SONDA N. 2.01: 31 UR% 
      SONDA N. 2.02: 1004 HPA 
      SONDA N. 2.03: 72.7 W/M2 
      SONDA N. 2.04: 0 GN 
      SONDA N. 3.01: 0 M/SEC 
      SONDA N. 3.02: 0 MMH2O 
      SONDA N. 1.05: 2.8 GC 
      SONDA N. 1.09: 8.9 GC 
      SONDA N. 2.05: 10 UR% 
      SONDA N. 2.09: 64 UR% 
      SONDA N. 2.06: 997 HPA 
      SONDA N. 2.10: 1004 HPA 
      FINE PROGR.40 
      </code>
<h3>Installazione su nuova raspberry</h3>
<ol>
  <li><a href="https://www.raspberrypi.org/downloads/">Sceli un OS</a> da installare sul raspberry, (io ho installato rasbian)
  </li>
  <li>Installa l'OS, seguendo i molti tutorial online se non sai come.
  </li>
  <li>		CLONE		
  </li>
  <li>		PERSISTENT
  </li>
  <li> 		CONFIG
  </li>
  <li>		
  </li>
  <li>
  </li>
</ol>
<h3>Note</h3>
   Leggere dati da usb é complesso, inizialmente avevo optato e sviluppato PureJavaHidApi in java ma per per ma dei conflitti con la libreria JNA sono stato obbligato a cambiare strada e a dirigermi sull molto piú comune pyserial scritto in python.
<h3>Configurazione</h3>
<ol>
  <li> Il Software é configurabile attraverso il file config.txt nella cartella src
  </li>
  
  <li> DETTAGLI
  </li>
</ol>

<h3>Idee per cose da sviluppare che puoi aggiungere</h3>
<ol>
  <li> Un'interfaccia seriale per leggere dalla stazione. </li>
  <li> un'interfaccia web per pubblicare i risultati. </li>
  <li> un database per contenere i dati. </li>
  <li> un modo per tenere sempre vivi i processi essenziali del raspberry, eseguirli all'avvio e aggiornare il software clonado questa repository (script?) </li>
  <li> un Bot per interfacciarsi con Messanger, Whatsapp e Telegram </li>
  <li> testare la sicurezza (ssh) </li>
  <li> Un sistema distribuito di stazioni meteo <a href="http://www.instructables.com/id/LoRaWan-Weather-Station/">Idea generale</a>, <a href="https://github.com/miky97it/Meteo/tree/master/Meteo">codice di Bortot Michele</a>, <a href="mailto:miky97it@gmail.com?Subject=MeteoPlanck" target="_top">piú info</a></li>
  <!--  
  <li>
    Inserisci qui punti che intendi sviluppare
  </li>
  -->
  
</ol>

<h3>Contribuisci</h3>
Non sai cosa portare come progetto d'esame ? vuoi migliorare la tua conoscenza di Java ? hai nuove idee per questo progetto ? Ecco come contribuire a questo progetto
<ol>
  <li> Avvisa il tuo professore di informatica o sistemi (se non sanno che pesci pigliare rivolgiti a quelli di un'alrta sezione). </li>
  <li> Presentati ai professori di fisica cosí da avere accesso al laboratorio e alla teca quando vuoi. </li>
  <li> Connettiti con:
     <ul>
        <li> ti connetti in laboratorio di fisica alla porta ethernet del pc fisso col tuo portatile, inserisci l'indirizzo fisso 
192.168.16.xxx con xxx >10 <254 e non 125 (provane un paio), via <a href="http://www.putty.org/">putty</a> ti colleghi a 192.168.16.125
        </li>
        <li>puoi anche fare il passaggio precedente la prima volta collegarlo ad un tuo hotspot e da allora in poi usare l'hotspot (memorizzato) con annesso ip
           per collegarti
        </li>
         <li>portatelo a casa e collegalo ad un monitor via HDMI. 
        </li>
     </ul>
   <li>
  
  Clona questa repository nel tuo git e carica lí i tuoi aggiornamenti
  </li>
</ol>
<h3>Ti sei bloccato in una di queste fasi ?</h3>
<a href="mailto:miky97it@gmail.com?Subject=MeteoPlanck" target="_top">scivimi (Bortot Michele)</a><!--metti qui il tuo nome -->
