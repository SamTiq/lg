class Piece:
    nom=""
    def __init__(self, pos, camp):
        self.pos = pos
        self.camp = camp
        self.has_moved = False
        if camp==1:
            self.couleur="blanc"
        else:
            self.couleur="noir"

    def get_pos(self):
        return self.pos

    def get_camp(self):
        return self.camp

    def move(self, pos):
        self.pos=pos
        self.has_moved=True

    
    def dessine(self):
        window_surface.blit(pieces_dict[self.nom+'_'+self.couleur], [(self.get_pos()[1]-1)*ratio, abs((self.get_pos()[0]-8)*ratio)])


class Cavalier(Piece):
    nom="cavalier"

    def premove(self, var):
        tab = [(self.pos[0]+2, self.pos[1]+1), (self.pos[0]+1, self.pos[1]+2), (self.pos[0]-2, self.pos[1]-1), (self.pos[0]-1, self.pos[1]-2), (self.pos[0]+1, self.pos[1]-2), (self.pos[0]+2, self.pos[1]-1), (self.pos[0]-2, self.pos[1]+1),  (self.pos[0]-1, self.pos[1]+2)]
        tab= game.check_limit(tab)
        for pos in tab:
            if game.find_case(pos)==self.camp and var == 0:
                tab.remove(pos)
        return tab