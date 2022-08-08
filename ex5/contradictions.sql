select distinct TranscationNo, ProductNo
from sales a1
where TranscationNo in
      (select TranscationNo
       from sales a2
       where (
                   a1.TranscationNo = a2.TranscationNo and
                   (a1.date != a2.date or a1.CustomerNo != a2.CustomerNo or a1.Country != a2.Country)
           )
          or EXISTS(
               select TranscationNo
               from sales a2
               where (a1.CustomerNo = a2.CustomerNo and a1.Country != a2.Country)
           )
          or EXISTS(
               select TranscationNo
               from sales a2
               where (a1.ProductNo = a2.ProductNo and
                      a1.ProductName != a2.ProductName)
           )
      )
order by TranscationNo, ProductNo;

