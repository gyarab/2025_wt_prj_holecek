# Mapa a hodnocení kebabáren (KebabTracker)

Django projekt KebabTracker slouží jako komunitní databáze a recenzní portál výhradně pro prodejce kebabu. Běžné mapy často ignorují reálnou kvalitu z pohledu strávníka. Můj specializovaný web podobný nedostatek naprosto eliminuje.

Návštěvníci do systému sami přidávají nové podniky a rovnou specifikují kompletní nabídku (döner, dürüm, falafel). Ke každému místu následně píšou detailní recenze. Hodnotitelé posuzují kvalitu masa, čerstvost zeleniny, chuť omáček, velikost porce i celkový poměr cena/výkon. Algoritmus z posbíraných dat automaticky vypočítá průměrné skóre a sestaví žebříček nejlepších bister.

Výsledný kód vytváří přehledný katalog s integrovaným filtrováním a vyhledáváním. Stránka nakonec naprosto každému pomůže najít bezkonkurenčně nejlepší kebab ve městě.

# Odborný článek: Projekt KebabTracker

Projekt KebabTracker představuje specializovaný informační <u>systém</u> a webovou <u>aplikaci</u> sloužící k evidenci, lokalizaci a <u>hodnocení</u> gastronomických provozoven, které primárně nabízejí <u>kebab</u>. Jádrem projektu je relační <u>databáze</u> uchovávající detailní záznamy o jednotlivých podnicích, obecně označovaných jako <u>kebabárny</u>.

Z hlediska interakce uživatelských rolí, definovaných architekturou navrženého uživatelského toku (User Flow) a drátěných modelů (Wireframes), systém striktně odděluje tři typy aktérů s odlišnými právy.

Anonymní <u>návštěvník</u> přistupuje na domovskou stránku, ze které naviguje buď do zobrazení textového seznamu, nebo na plátno interaktivní <u>mapy</u>. Pro efektivní vyhledávání využívá vestavěné <u>filtry</u> umožňující omezit výsledky na základě lokality (město), průměrného <u>skóre</u>, aktuální otevírací doby, cenové hladiny nebo preferovaného druhu <u>masa</u>. Po výběru konkrétního podniku se zobrazí <u>detail</u> provozovny obsahující <u>adresu</u>, kompletní <u>menu</u> a historii existujících uživatelských recenzí. Anonymní přístup umožňuje výhradně čtení dat.

Registrovaný <u>uživatel</u> podstupuje proces autentizace. Tím získává oprávnění modifikovat <u>obsah</u>. Z obrazovky detailu podniku smí vložit novou <u>recenzi</u>. Tento proces vyžaduje zadání celkového hvězdičkového hodnocení a umožňuje specifikovat dílčí známky pro klíčové <u>suroviny</u>, konkrétně maso a <u>omáčky</u>. Součástí formuláře je textový <u>komentář</u> a volitelný upload obrazového materiálu (<u>fotografie</u>). Registrovaný aktér má rovněž právo navrhnout zařazení dosud neevidovaného podniku. Osobní <u>profil</u> agreguje jeho aktivitu, zobrazuje počet napsaných recenzí, uložené podniky a průměrný udělený rating.

<u>Administrátor</u> přistupuje po přihlášení do zabezpečeného administračního panelu (<u>Dashboardu</u>). Zde provádí globální správu platformy. Rozhraní obsahuje nástroje pro plný přístup k centrální správě uživatelů, moderaci textů a fotografií v recenzích a přímou editaci či zakládání nových záznamů o podnicích.
![IMG_20260306_081712](https://github.com/user-attachments/assets/2fe93f93-2286-42f0-82be-5adad7301023)
![IMG_20260306_081647](https://github.com/user-attachments/assets/449d96dd-43f3-4efc-8d2f-2773ff0b443e)
![IMG_20260313_085331](https://github.com/user-attachments/assets/6da1b94f-66a4-48d0-addc-c7be6929623c)
