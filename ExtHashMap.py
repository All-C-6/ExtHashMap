import re

class ExtendedHashMap(dict):

    def key(self, k):
        return k in self.__dict__

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __iter__(self):
        return iter(self.__dict__)

        def __sorting(self, sorted_list):

            for i in range(len(sorted_list)):

                if sorted_list[i].count(",") > 0:

                    if not sorted_list[i][0].isdigit():
                        sorted_list[i] = sorted_list[i][1:-1]
                    sorted_list[i] = tuple(map(int, sorted_list[i].split(',')))

                elif sorted_list[i][0].isdigit():
                        sorted_list[i] = tuple(map(int, sorted_list[i]))

            return sorted_list

        def iloc(self, val = None):
            sort_dict = sorted(list(self.__dict__.items()))
            res_dict = [i[1] for i in sort_dict]

            if val is None:
                return res_dict

            return self.__dict__

        def conditionProc(self, operator, operand, pos, sorted_list):

            match operator:
                case ">=":
                    return set(filter(lambda x: int(x[pos]) >= operand, sorted_list))

                case ">":
                    return set(filter(lambda x: int(x[pos]) > operand, sorted_list))

                case "<":
                    return set(filter(lambda x: int(x[pos]) < operand, sorted_list))

                case "<=":
                    return set(filter(lambda x: int(x[pos]) <= operand, sorted_list))

                case "==":
                    return set(filter(lambda x: int(x[pos]) == operand, sorted_list))

                case "<>":
                    return set(filter(lambda x: int(x[pos]) != operand, sorted_list))
                case _:
                    raise ValueError("Wrong condition")

        def ploc(self, *args):
            string = str(*args)
            list_conditions = []
            item_condition = ''

            if string == '':
                raise ValueError("Wrong condition")

            for i in range(len(string)):

                if string[len(string) - 1].isdigit() == False:
                    raise ValueError("Wrong condition")

                if re.match("[>|<|=]?", string[i]).span() != (0, 0):
                    item_condition += string[i]
                    continue

                if string[i].isdigit():
                    item_condition += string[i]

                    if len(item_condition) > 0:

                        if item_condition[0].isdigit():
                            raise ValueError("Wrong condition")
                    list_conditions.append(item_condition)
                    item_condition = ''

            return self.__ploc_dop(list_conditions)

