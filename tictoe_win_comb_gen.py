def win_combo(n):
   if n < 1:
      return -1

   tic_tac_win_combo = []

   for i in range(n):
      row = [j  for j in range(i * n, (i + 1) * n)]
      col = [j  for j in range(i, n * n, n)]
      tic_tac_win_combo.append(row)
      tic_tac_win_combo.append(col)

   diagonal1 = [i  for i in range(n * n) if i % (n + 1) == 0]
   diagonal2 = [i  for i in range(n * n) if i % (n - 1) == 0 and i != 0 and i != (n * n - 1)]
   tic_tac_win_combo.append(diagonal1)
   tic_tac_win_combo.append(diagonal2)

   return tic_tac_win_combo

print(win_combo(3))
