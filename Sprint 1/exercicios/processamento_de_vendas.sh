#!/bin/bash

cd ecommerce
mkdir vendas
cp dados_de_vendas.csv vendas/dados_de_vendas.csv
cd vendas
mkdir backup
cp dados_de_vendas.csv backup/dados-$(date +"%d%m%Y").csv
cd backup
mv dados-$(date +"%d%m%Y").csv backup-dados-$(date +"%Y%m%d").csv
touch relatorio-$(date +"%d-%m-%Y").txt
echo "-------------------------------------------------">> relatorio-$(date +"%d-%m-%Y").txt
echo "Relatório de vendas" >> relatorio-$(date +"%d-%m-%Y").txt
echo "-------------------------------------------------">> relatorio-$(date +"%d-%m-%Y").txt
echo "Data e horario: " >> relatorio-$(date +"%d-%m-%Y").txt
(date +"%Y/%m/%d %H:%M") >> relatorio-$(date +"%d-%m-%Y").txt
echo "-------------------------------------------------">> relatorio-$(date +"%d-%m-%Y").txt
echo "" >> relatorio-$(date +"%d-%m-%Y").txt
echo "Data do primeiro  registro de vendas: " >> relatorio-$(date +"%d-%m-%Y").txt
cut -d ',' -f5 backup-dados-$(date +"%Y%m%d").csv | sed '1d;s/-/\//g' | sort -r -t/ -k3,3 -k2,2 -k1,1 | tail -n 1 >> relatorio-$(date +"%d-%m-%Y").txt
 echo "-------------------------------------------------">> relatorio-$(date +"%d-%m-%Y").txt
 echo "" >> relatorio-$(date +"%d-%m-%Y").txt
echo "Data do ultimo registro de vendas: " >> relatorio-$(date +"%d-%m-%Y").txt
cut -d ',' -f5 backup-dados-$(date +"%Y%m%d").csv | sed '1d;s/-/\//g' | sort -t '/' -k3,3n -k2,2n -k1,1n | tail -n 1 >> relatorio-$(date +"%d-%m-%Y").txt
 echo "-------------------------------------------------">> relatorio-$(date +"%d-%m-%Y").txt
 echo "" >> relatorio-$(date +"%d-%m-%Y").txt
echo "Quantidade de itens diferentes vendidos: " >> relatorio-$(date +"%d-%m-%Y").txt
awk -F ',' 'NR>1 {print $2}' backup-dados-$(date +"%Y%m%d").csv | sort | uniq -c | wc -l >> relatorio-$(date +"%d-%m-%Y").txt
echo "-------------------------------------------------">> relatorio-$(date +"%d-%m-%Y").txt
echo "" >> relatorio-$(date +"%d-%m-%Y").txt
echo " As 10 primeiras linhas da tabela Dados de vendas" >> relatorio-$(date +"%d-%m-%Y").txt
echo "" >> relatorio-$(date +"%d-%m-%Y").txt
head -n10 backup-dados-$(date +"%Y%m%d").csv >> relatorio-$(date +"%d-%m-%Y").txt
echo "-------------------------------------------------">> relatorio-$(date +"%d-%m-%Y").txt
echo "" >> relatorio-$(date +"%d-%m-%Y").txt
echo "" >> relatorio-$(date +"%d-%m-%Y").txt
gzip -c backup-dados-$(date +"%Y%m%d").csv > backup-dados-$(date +"%Y%m%d").csv.gz
rm backup-dados-$(date +"%Y%m%d").csv
rm ../dados_de_vendas.csv
cat relatorio-$(date +"%d-%m-%Y").txt





