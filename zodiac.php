<?php
        $zodiac = ["zodiac.webp",'aries.jpeg', "taurus.jpg","gemini.webp","cancer.jpg","leo.jpg", "virgo.jpeg","libra.webp", "scorpio.jpeg",
        "sagit.jpeg", "capricorn.jpg","aquarius.jpg","piesc.jpg"];
        $data = "<html><head><link rel=stylesheet href=style.css /><link rel=icon href=zodiac.webp/></head><body><center class=cell-decoration>"."Daily Horoscope : ".date("l jS \of F Y ")."<br/><table>\n\n"; 
      
        $file = fopen("scrape.csv", "r"); 
        $j=0;
 
        while (($csv = fgetcsv($file)) !== false) { 
            $data = $data."<tr>"; 
            $data=$data."<td ><img class=img-pos src='".$zodiac[$j]."' /></td>";  
            foreach ($csv as $i) { 
                $data = $data."<td class = cell-decoration>".$i. "</td>"; 
            } 
           $data =  $data."</tr> \n";
           $j++;
        } 
        fclose($file); 
        $data = $data."\n</table></center></body></html>"; 
              file_put_contents("index.html", $data);
  ?>