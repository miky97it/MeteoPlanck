# MeteoPlanck
This project is operative on the meteo station of the institute ITIS Max Planck in Lancenigo of Villorba near Treviso.
<h1>Stazione Meteo ITIS Max Planck </h1>
<h3>Obbiettivi</h3>
Tenere aggiornata la Stazione Meteo d'anno in anno pubblicando i dati sulle piú moderne piattaforme
<h3>Funzionamento</h3>
<ol>
  <li>il sito (inserisci link pagina) é hostato su git.
  </li>
  <li>Una Raspberry esegue un sofware che:
    <ol>
      <li>Legge dalla stazione meteo analogica in Laboratorio di fisica i dati e gli salva in un database NoSQL MongoDB
      </li>
      <li>Risponde alle chiamate degli utenti (intermediate dal sito del Planck) sotto forma di API Json.
      </li>
      <li>Si auto aggiorna clonando questa repository
      </li>
      <li>Ha un sistema anti-crash.
      </li>
    </ol>
  </li>
  <li>Il sito del Planck fa da intermediario tra gli utenti e il raspberry prensentando le API (link)
  </li>
</ol>
<h3>Punti da sviluppare</h3>
<ol>
  <li>
    Un'interfaccia seriale per leggere dalla stazione.
  </li>
  <li>
    un'interfaccia web per pubblicare i risultati.
  </li>
  <li>
    un database per contenere i dati.
  </li>
  <li>
    un modo per tenere sempre vivi i processi essenziali del raspberry, eseguirli all'avvio e aggiornare il software clonado questa repository (script?)
  </li>
  <li>
    aggiungere un file di configurazione
  </li>
  <li>
    un Bot per interfacciarsi con Messanger, Whatsapp e Telegram
  </li>
  <li>
    testare la sicurezza (ssh)
  </li>
  <li>
    Un sistema distribuito di stazioni meteo <a href="http://www.instructables.com/id/LoRaWan-Weather-Station/">Idea generale</a>, <a href="https://github.com/miky97it/Meteo/tree/master/Meteo">codice di Bortot Michele</a>, <a href="mailto:miky97it@gmail.com?Subject=MeteoPlanck" target="_top">piú info</a>
  </li>
  
  <!--  
  <li>
    Inserisci qui punti che intendi sviluppare
  </li>
  -->

</ol>
<h3>Contribuisci</h3>
Non sai cosa portare come progetto d'esame ? vuoi migliorare la tua conoscenza di Java ? hai nuove idee per questo progetto ? Ecco come contribuire a questo progetto
<ol>
  <li>
    Avvisa il tuo professore di informatica o sistemi (se non sanno che pesci pigliare rivolgiti a quelli di un'alrta sezione).
  </li>
  <li>
    Presentati ai professori di fisica cosí da avere accesso al laboratorio e alla teca quando vuoi.
  </li>
  <li>
    Connettiti con un portatile al rasperry via <a href="http://www.putty.org/">putty</a> o portatelo a casa e collegalo ad un monitor via HDMI
  </li>
    Clona questa repository nel tuo git e carica lí i tuoi aggiornamenti
  </li>
</ol>
<h3>Sviluppatori</h3>
2018 Bortot Michele "97 5Aii <a href="mailto:miky97it@gmail.com?Subject=MeteoPlanck" target="_top">email</a>
<!--metti qui il tuo nome -->

