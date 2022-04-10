Kontrat Spesifikasyonu: 

State Variables: 

1.	Owner (kontrat sahibi, public)
2.	userBalance (kontrat bakiyesi, private)
3.	withdrawAmount (çekmek istediğimiz miktar, public)
4.	canWithdraw (çekimin geçerli olup olmadığı; True, False, public)

Functions:

1.	Constructor (Owner’ı kontratı deploy eden kişi yapmalı)
2.	withdrawAmount için bir setter fonksiyon
3.	userBalance için bir setter fonksiyon
4.	userBalance için bir getter fonksiyon (sadece Owner çağırabilmeli bu fonksiyonu, if statement kullanarak sağlanmalı bu kural)
5.	withdrawAmount’ı, userBalance ile kıyaslayıp canWithdraw’ı güncelleyecek fonksiyon 	

Fonksiyonlar doğru şekilde view ya da pure olarak etiketlenmeli.

