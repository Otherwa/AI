 if (a + b <= y):
            if (get_all_states((0, a + b, c))):
                ans.append(state)
                return True
        else:
            if (get_all_states((a - (y-b), y, c))):
                ans.append(state)
                return True