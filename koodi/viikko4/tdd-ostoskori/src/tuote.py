class Tuote:
  def __init__(self, nimi: str, hinta: int):
      self.nimi = nimi
      self.hinta = hinta
      self.saldo = 0

  def hinta(self):
    return self._hinta

  def nimi(self):
    return self._nimi

  def __repr__(self):
      return f"{self.nimi} hinta {self.hinta} euroa"