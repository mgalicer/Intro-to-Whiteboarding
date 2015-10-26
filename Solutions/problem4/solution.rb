int i = 0;
int j = 0;

while (str[i] != null){
  while(from[j] != null){
    if (from[j] == str[i]){
    str[i] = to[j];
  }
  i++;
  }
  j++;
}
