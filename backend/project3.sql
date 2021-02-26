CREATE TABLE Customers
(
	cust_id VARCHAR(64) PRIMARY KEY NOT NULL,
	cust_name VARCHAR(50) NOT NULL,
	cust_email VARCHAR(50) NOT NULL,
	cust_phone VARCHAR(10) NOT NULL,
	credential VARCHAR(30) NOT NULL
);

CREATE TABLE Restaurant
(
	rID VARCHAR(64) PRIMARY KEY NOT NULL,
	rName VARCHAR(50) NOT NULL,
	rCuisine VARCHAR(50) NOT NULL,
	rPhone VARCHAR(10) NOT NULL,
	rLatitude DECIMAL(20,7) NOT NULL,
    rLongitude DECIMAL(20,7) NOT NULL,
	rRating DECIMAL(2,1) NOT NULL,
	cuisine_qty INTEGER
);

CREATE TABLE Orders
(
	order_id VARCHAR(64) PRIMARY KEY NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    order_quantity INTEGER NOT NULL,
    cust_id VARCHAR(64) FOREIGN KEY REFERENCES Customers(cust_id),
    rID VARCHAR(64) FOREIGN KEY REFERENCES Restaurant(rID)
);

INSERT INTO Restaurant (rID, rName, rCuisine, rPhone, rLatitude, rLongitude, rRating, cuisine_qty) VALUES
('1ow7277jgn13w5i9u4howyj5qjjmmypewojtv8pwvjrjx902v03m8zs182wewhhb', 'R1', 'Indian', '5211198870', 47.6239122, -122.3356781, 4.0, 15),
('keyvgz56hizj7jd8djotfmvlh4it73uyaibiu2o68q00lcvyojy58k9hytre2vsy', 'R2', 'Italian', '4557682231', 47.6226383, -122.3377189, 3.5, 20),
('yjmg2si4e7mfe7mm1q516moaksi9kir7ks27sdtds8j7ix1qfe006n2kxf6a4em4', 'R3', 'British', '8722127616', 47.6236507, -122.3364272, 3.0, 50),
('g2xztergwiw7i8o4eqtnxnyhd85da4esyfkl8bi60zlbwz9olcnzr1xiv64sqx8i', 'R4', 'American', '4239096408', 47.6238214, -122.3416500, 4.5, 20),
('8j57hkdcalhqcnffezgf7ke2h9xu7xqltiyk5hapod0mg438gh0528jbkspr09cg', 'R5', 'Spanish', '3668933760', 47.6166070, -122.3429246, 3.5, 22),
('arsps45vq0vmwyrt2202fs9z2b0mdoo56x89hpe44gr4e5x7iblnpxqnndd17q2t', 'R6', 'Indian', '0730252405', 47.6167893, -122.3396502, 4.5, 30),
('xsvyoxsc8w2io2lrzdkpnnyrvz0e522tp69fqy92xdw7eynth05p7ld59bn6frbt', 'R7', 'Chinese', '1742933552', 47.6162252, -122.3398862, 4.2, 35),
('r76uzsfmijohthjcevrcqwcjh1ydsj5x0caa9l279gjzfcq4h79xmj32iapvljmt', 'R8', 'Japanese', '1121682299', 47.6218226, -122.3367534, 4.0, 17),
('9wvo61nj4m28cojww4fbvewbl3g2k0vsgusyduu9lbfjvxcm8yop2tgofses3vjl', 'R9', 'Mexican', '2424905651', 47.6215392, -122.3323116, 4.2, 20),
('49s25nvxlksftgmh5a89jo2bf2trgurxur5exgd8rh9e0vjtn0s2xnonktekqskn', 'R10', 'Greek', '6107972792', 47.6248771, -122.3258786, 4.0, 30);

INSERT INTO Orders (order_id, order_quantity, cust_id, rID) VALUES
('oid100', 1, 'cs001', '1ow7277jgn13w5i9u4howyj5qjjmmypewojtv8pwvjrjx902v03m8zs182wewhhb'),
('oid101', 2, 'cs0010', 'arsps45vq0vmwyrt2202fs9z2b0mdoo56x89hpe44gr4e5x7iblnpxqnndd17q2t'),
('oid102', 1, 'cs004', 'xsvyoxsc8w2io2lrzdkpnnyrvz0e522tp69fqy92xdw7eynth05p7ld59bn6frbt'),
('oid103', 2, 'cs005', 'xsvyoxsc8w2io2lrzdkpnnyrvz0e522tp69fqy92xdw7eynth05p7ld59bn6frbt'),
('oid104', 1, 'cs007', '9wvo61nj4m28cojww4fbvewbl3g2k0vsgusyduu9lbfjvxcm8yop2tgofses3vjl'),
('oid105', 1, 'cs008', '49s25nvxlksftgmh5a89jo2bf2trgurxur5exgd8rh9e0vjtn0s2xnonktekqskn'),
('oid106', 1, 'cs009', '9wvo61nj4m28cojww4fbvewbl3g2k0vsgusyduu9lbfjvxcm8yop2tgofses3vjl'),
('oid107', 2, 'cs005', 'keyvgz56hizj7jd8djotfmvlh4it73uyaibiu2o68q00lcvyojy58k9hytre2vsy'),
('oid108', 2, 'cs006', 'arsps45vq0vmwyrt2202fs9z2b0mdoo56x89hpe44gr4e5x7iblnpxqnndd17q2t'),
('oid109', 1, 'cs008', '9wvo61nj4m28cojww4fbvewbl3g2k0vsgusyduu9lbfjvxcm8yop2tgofses3vjl');



