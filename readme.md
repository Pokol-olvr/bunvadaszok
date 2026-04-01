##Bűnvadászok checker

Repo elemei:
- Google Cloud-ban létrehozott API kulcs
- Python GET metódus -> JSON
- JSON tárolás/olvasás/írás
- Slack üzenet küldés
- GitHub actions automatizáció cron jobbal és ruff/lint

A korábban felsorolt elemek workflowját itt részletezem.
Elsősorban a GitHub secretekben tárolt kulcsokkal és az API-val egy JSON formájában megkapjuk a legfrisebben feltöltött videót és annak attribútumait.
csatorna id, leírás, feltöltés dátuma, videó címe, csatorna címe

Ezt egy video.json fileba tároljuk, későbbi olvasásra.
Minden 2. órában elindul a workflow és megvizsgálja a tárolt JSON videó feltöltési dátumát és összehasonlítja a friss hívás dátumával.
Ha az új hívás dátuma frissebb akkor a tárolt JSON-t felülírja és elhelyezi a POST metódusba mint üzenet, amit a beállított slack bot elküld egy slack thread-be.
A lezajlott változattásokat automatikusan pusholja és mergeli az eredeti branchre.

Ezen kívül a zajló fejlesztés bugfix esetén egy linter action is be van állítva ami minden pull requestre lefut és vizsgálja a kódot.
Szükség esetén pedig automatikusan javítja és nyit egy pull requestet amit nekünk kell jóváhagyni.
