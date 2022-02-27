-- Make some artists
INSERT INTO artist 
        VALUES(Null,"Vincent", 'Van Gogh','1853-03-30','Netherlands','1890-07-29');
INSERT INTO artist 
        VALUES(Null,"Andy", 'Warhol','1928-08-06','USA','1987-02-22');
INSERT INTO artist 
        VALUES(Null,"Richard", 'Diebenkorn','1922-04-22','USA','1993-03-30');

-- Add some museums
INSERT into museum
      VALUES(Null,"Berkeley Art", "USA","Berkeley");
INSERT into museum
      VALUES(Null,"de Young", "USA","San Francisco");

-- Load in some Diebenkorns
INSERT INTO work 
  VALUES(Null,3,"Seawall","Painting",2,"1957-06-01");
INSERT INTO work 
    VALUES(Null,3,"Spreading Spade","Print",1,"1981-02-30");

-- Load in some Van Gogh (currently at the de Young!)
INSERT INTO work 
      VALUES(Null,1,"Bedroom at Arles","Painting",2,"1889-09-03");  
                  
-- Load in some Warhol
INSERT INTO work 
    VALUES(Null,2,"Campbell's Tomato Soup (from a banner)","screenprint",2,"1968-09-08");
INSERT INTO work 
        VALUES(Null,2,"Liz","lithograph",1,"1966-02-22");
