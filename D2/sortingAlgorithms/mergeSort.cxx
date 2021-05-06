// tri par fusion

void fusion(int *t, int deb1, int fin1, int fin2)
{
  int *table1;
  int deb2 = fin1 + 1;
  int compt1 = deb1;
  int compt2 = deb2;
  int i;
  table1 = (int *) malloc((fin1 - deb1 + 1) * sizeof(int));
  for (i = deb1; i <= fin1; i++)
    table1[i - deb1] = t[i];
  for (i = deb1; i <= fin2; i++)
  {
    if (compt1 == deb2)
      break;
    else if (compt2 == (fin2 + 1))
    {
      t[i] = table1[compt1 - deb1];
      compt1++;
    }
    else if (table1[compt1 - deb1] < t[compt2])
    {
      t[i] = table1[compt1 - deb1];
      compt1++;
    }
    else
    {
      t[i] = t[compt2];
      compt2++;
    }
  }
  free(table1);
}
void tri_fusion_bis(int *t, int deb, int fin)
{
  if (deb != fin)
  {
    int milieu = (fin + deb) / 2;
    tri_fusion_bis(t, deb, milieu);
    tri_fusion_bis(t, milieu + 1, fin);
    fusion(t, deb, milieu, fin);
  }
}
void tri_fusion(int *t, int n)
{
  if (n > 0)
    tri_fusion_bis(t, 0, n - 1);
}
