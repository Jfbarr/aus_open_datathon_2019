# Defines the probability player A wins a game on their serve
# p_a is the probability of a win, q_a the probability of a loss
def game_win_a(p_a):
    q_a = 1-p_a
    return p_a**4 * (1+ 4*q_a+10*(q_a**2)) + 20*(p_a*q_a)**3 *p_a**2 *(1-2* p_a*q_a)**(-1)

# Calculated values for p_set_a_i_j, the probability player a wins the set on game (i,j) give A serves first

### game_a = game_win_a(p_a), and game_b =game_win_b(p_b)
def p_set_a_6_0(p_game_a, p_game_b):
    q_game_a = 1 - p_game_a
    q_game_b = 1 - p_game_b
    return (p_game_a * q_game_b)**3

def p_set_a_6_1(p_game_a, p_game_b):
    q_game_a = 1 - p_game_a
    q_game_b = 1 - p_game_b
    return 3*p_game_a**3 *q_game_a *q_game_b**3 + 3 *(p_game_a)**4 * p_game_b * (q_game_b)**2
    
def p_set_a_6_2(p_game_a, p_game_b):
    q_game_a = 1 - p_game_a
    q_game_b = 1 - p_game_b
    return 12* (p_game_a)**3 * q_game_a * p_game_b * (q_game_b)**3 \
    + 6*(p_game_a)**2*(q_game_a)**2 *(q_game_b)**4 + 3*(p_game_a)**4 *(p_game_b)**2 *(q_game_b)**2
        
def p_set_a_6_3(p_game_a, p_game_b):
    q_game_a = 1 - p_game_a
    q_game_b = 1 - p_game_b
    return 24*(p_game_a)**3 *(q_game_a)**2 * p_game_b * (q_game_b)**3 + 24*(p_game_a)**4 * q_game_a *(p_game_b)**2 *(q_game_b)**2 \
        +4 *(p_game_a)**2 *(q_game_a)**3 *(q_game_b)**4 + 4 *(p_game_a)**5*(p_game_b)**3 *q_game_b
        
def p_set_a_6_4(p_game_a, p_game_b):
    q_game_a = 1 - p_game_a
    q_game_b = 1 - p_game_b
    return 60*(p_game_a)**3 *(q_game_a)**2 * (p_game_b)**2 *(q_game_b)**3 \
        + 40*(p_game_a)**2 *(q_game_a)**3 *(p_game_b) *(q_game_b)**4 \
        + 20*(p_game_a)**4*q_game_a*(p_game_b)**3*(q_game_b)**2 + 5*p_game_a * (q_game_a)**4 *(q_game_b)**5 \
        + p_game_a**5*(p_game_b)**4 *q_game_b
        
def p_set_a_7_5(p_game_a, p_game_b):
    q_game_a = 1 - p_game_a
    q_game_b = 1 - p_game_b
    return 100 * (p_game_a)**3*(q_game_a)**3 *(p_game_b)**2 * (q_game_b)**4 \
        + 100*(p_game_a)**4*(q_game_a)**2*(p_game_b)**3*(q_game_b)**3 \
        + 25*(p_game_a)**2*(q_game_a)**4*p_game_b * (q_game_b)**5 \
        + 25*(p_game_a)**5*q_game_a*(p_game_b)**4*(q_game_b)**2 \
        + p_game_a *(q_game_a)**5 * (q_game_b)**6 + (p_game_a)**6*(p_game_b)**5*q_game_b
        
        
def p_set_a_6_6(p_game_a, p_game_b):
    return 1 - ((  p_set_a_6_0(p_game_a, p_game_b)   + p_set_a_6_0(p_game_b, p_game_a) \
                +  p_set_a_6_1(p_game_a, p_game_b) + p_set_a_6_1(p_game_b, p_game_a) \
                +  p_set_a_6_2(p_game_a, p_game_b) + p_set_a_6_2(p_game_b, p_game_a) \
                +  p_set_a_6_3(p_game_a, p_game_b) + p_set_a_6_3(p_game_b, p_game_a) \
                +  p_set_a_6_4(p_game_a, p_game_b) + p_set_a_6_4(p_game_b, p_game_a))\
               + p_set_a_7_5(p_game_a, p_game_b) + p_set_a_7_5(p_game_b, p_game_a))


    
def p_tie_a_7_0(p_a, p_b):
    q_a = 1 - p_a
    q_b = 1 - p_b
    return (p_a)**3 *(q_b)**4

def p_tie_a_7_1(p_a, p_b):
    q_a = 1 - p_a
    q_b = 1 - p_b
    return 3* (p_a)**3 *q_a *(q_b)**4 + 4*(p_a)**4 *p_b *(q_b)**3
    
def p_tie_a_7_2(p_a, p_b):
    q_a = 1 - p_a
    q_b = 1 - p_b
    return 16*(p_a)**4 *q_a*p_b*(q_b)**3 + 6 *(p_a)**5 *(p_b)**2 *(q_b)**2 + 6 *(p_a)**3 *(q_a)**2*(q_b)**4
    
def p_tie_a_7_3(p_a, p_b):
    q_a = 1 - p_a
    q_b = 1 - p_b
    return 40*(p_a)**3*(q_a)**2*p_b*(q_b)**4 + 10*(p_a)**2*(q_a)**3*(q_b)**5 \
        +4*(p_a)**5*(p_b)**3*(q_b)**2 + 30*(p_a)**4*q_a*(p_b)**2*(q_b)**3
    
def p_tie_a_7_4(p_a, p_b):
    q_a = 1 - p_a
    q_b = 1 - p_b
    return 50*(p_a)**4*q_a*(p_b)**3*(q_b)**3 + 5 *(p_a)**5*(p_b)**4 *(q_b)**2 \
        + 50 *(p_a)**2*(q_a)**3*p_b*(q_b)**5 + 5*p_a*(q_a)**4 * (q_b)**6 + 100*(p_a)**3*(q_a)**2*(p_b)**2*(q_b)**4
    
    
def p_tie_a_7_5(p_a, p_b):
    q_a = 1 - p_a
    q_b = 1 - p_b
    return 30*(p_a)**2*(q_a)**4*p_b*(q_b)**5+p_a*(q_a)**5*(q_b)**6 +200*(p_a)**4*(q_a)**2*(p_b)**3*(q_b)**3 \
        + 75*(p_a)**5*q_a*(p_b)**4*(q_b)**2 + 150*(p_a)**3*(q_a)**3*(p_b)**2*(q_b)**4 \
        + 6*(p_a)**6*(p_b)**5*q_b
        
def p_tie_a_6_6(p_a, p_b):
    q_a = 1 - p_a
    q_b = 1 - p_b
    return 1 - ( p_tie_a_7_0(p_a, p_b) + p_tie_a_7_0(q_a, q_b) \
               + p_tie_a_7_1(p_a, p_b) + p_tie_a_7_1(q_a, q_b)  \
               + p_tie_a_7_2(p_a, p_b) + p_tie_a_7_2(q_a, q_b)  \
               + p_tie_a_7_3(p_a, p_b) + p_tie_a_7_3(q_a, q_b)  \
               + p_tie_a_7_4(p_a, p_b) + p_tie_a_7_4(q_a, q_b)  \
               + p_tie_a_7_5(p_a, p_b) + p_tie_a_7_5(q_a, q_b)  )
        
# p_A**T
#  p_set_a = p_A**6(6,j) + p_A**S(7,5) + p_A**S(6,6) p_A**T
def p_tie_win_a(p_a, p_b):
    q_a = 1-p_a
    q_b = 1-p_b
    return p_tie_a_7_0(p_a, p_b)+ p_tie_a_7_1(p_a, p_b) + p_tie_a_7_2(p_a, p_b) \
        +p_tie_a_7_3(p_a, p_b)+ p_tie_a_7_4(p_a, p_b) + p_tie_a_7_5(p_a, p_b) \
        + p_tie_a_6_6(p_a, p_b)*p_a*q_b *(1- p_a*p_b - q_a*q_b)**(-1)
        
def p_set_win_a(p_a, p_b):
    p_game_a = game_win_a(p_a)
    p_game_b = game_win_a(p_b)
    return p_set_a_6_0(p_game_a, p_game_b) + p_set_a_6_1(p_game_a, p_game_b) \
        + p_set_a_6_2(p_game_a, p_game_b) + p_set_a_6_3(p_game_a, p_game_b) \
        + p_set_a_6_4(p_game_a, p_game_b) + p_set_a_7_5(p_game_a, p_game_b)\
        + p_set_a_6_6(p_game_a, p_game_b)*p_tie_win_a(p_a, p_b)
    
    
def match_win_2_of_3(p_a, p_b):
    return (p_set_win_a(p_a, p_b))**2 + 2*(p_set_win_a(p_a,p_b))**2 * p_set_win_a(p_b,p_a)
    
def match_win_3_of_5(p_a, p_b):
    return (p_set_win_a(p_a,p_b) )**3 +3*(p_set_win_a(p_a,p_b))**3*p_set_win_a(p_b, p_a) \
            + 6*(p_set_win_a(p_a, p_b))**3 *(p_set_win_a(p_b, p_a))**2