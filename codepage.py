codepage = "λ¬∧⟑∨⟇÷«»°\n․⍎½∆øÏÔÇæʀʁɾɽÞƈ∞⫙ß⎝⎠ !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⎡⎣⨥⨪∺❝ð£¥§¦¡∂ÐřŠč√∖ẊȦȮḊĖẸṙ∑Ṡİ•\t"
codepage += "Ĥ⟨⟩ƛıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘŚśŜŝŞşšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƊƋƌƍƎ¢≈Ωªº"

commands = {
    '!': 'stack.push(len(stack))',
    '"': 'stack.shift(_RIGHT)',
    "'": 'stack.shift(_LEFT)',
    '$': 'stack.swap()',
    '%': 'rhs, lhs = stack.pop(2); stack.push(modulo(lhs, rhs))',
    '&': 'if VY_reg_reps % 2:VY_reg=stack.pop()\nelse:stack.push(VY_reg)\nVY_reg_reps += 1',
    '*': 'rhs, lhs = stack.pop(2); stack.push(multiply(lhs, rhs))',
    '+': 'rhs, lhs = stack.pop(2); stack.push(add(lhs, rhs))',
    ',': 'print(stack.pop(), end=""); printed = True',
    '-': 'rhs, lhs = stack.pop(2); stack.push(subtract(lhs, rhs))',
    '.': 'print(Vy_repr(stack.pop()), end=""); printed = True',
    '/': 'rhs, lhs = stack.pop(2); stack.push(divide(lhs, rhs))',
    ':': 'top = stack.pop(); stack.push(top); stack.push(top)',
    '<': 'rhs, lhs = stack.pop(2); stack.push(int(rhs < lhs))',
    '=': 'rhs, lhs = stack.pop(2); stack.push(int(rhs == lhs))',
    '>': 'rhs, lhs = stack.pop(2); stack.push(int(rhs > lhs))',
    '?': 'stack.push(get_input())',
    'A': 'stack.push(stack.all())',
    'B': 'stack.push(Vy_int(stack.pop(), 2))',
    'C': 'stack.push(chrord(stack.pop()))',
    'D': 'top = stack.pop(); stack.push(top); stack.push(top); stack.push(top)',
    'E': 'x = stack.pop(); stack.push(eval(x))',
    'F': 'stack.do_filter(stack.pop())',
    'G': 'stack.push(max(stack.pop()))',
    'H': 'stack.push(Vy_int(stack.pop(), 16))',
    'I': 'stack.push(Vy_int(stack.pop()))',
    'J': 'rhs, lhs = stack.pop(2); stack.push(join(lhs, rhs))',
    'K': 'stack.push(divisors_of(stack.pop()))',
    'L': 'stack.push(len(stack.pop()))',
    'M': 'stack.do_map(stack.pop())',
    'N': 'top = stack.pop(); stack.push(to_number(top))',
    'O': 'lhs, rhs = stack.pop(2); stack.push(as_iter(rhs).count(lhs))',
    'P': 'y, x = stack.pop(2); stack.push(str(x).strip(str(y)))',
    'Q': 'exit()',
    'R': 'TODO',
    'S': 'stack.push(str(stack.pop()))',
    'T': 'stack.push([n for n in stack.pop() if bool(n)])',
    'U': 'TODO',
    'V': 'replacent, needle, haystack = stack.pop(3); stack.push(haystack.replace(needle, replacent))',
    'W': 'lhs, rhs = stack.pop(2); stack.push(textwrap.wrap(rhs, lhs))',
    'X': 'if _context_level + 1 < _max_context_level: _context_level += 1',
    'Y': 'TODO',
    'Z': 'lhs, rhs = stack.pop(2); stack.push(list(zip(rhs, lhs)))',
    '^': 'stack.reverse()',
    '_': 'stack.pop()',
    '`': 'stack.push("{}")',
    'a': 'stack.push(any(stack.pop()))',
    'b': 'stack.push(bin(stack.pop()))',
    'c': 'lhs, rhs = stack.pop(2); stack.push(rhs in lhs)',
    'd': 'stack.push(stack.pop() * 2)',
    'e': 'lhs, rhs = stack.pop(2); stack.push(rhs ** lhs)',
    'f': 'stack.push(flatten(stack.pop())',
    'g': 'stack.push(VY_source[stack.pop()])',
    'h': 'stack.push(stack.pop()[0])',
    'i': 'lhs, rhs = stack.pop(2); stack.push(as_iter(rhs)[lhs])',
    'j': 'lhs, rhs = stack.pop(2); stack.push(lhs.join([str(_item) for _item in as_iter(rhs)])); ',
    'l': 'stack.push([])',
    'm': 'TODO',
    'n': 'stack.push(eval(f"_context_{_context_level}"))',
    'o': 'needle, haystack = stack.pop(2); stack.push(haystack.replace(needle, ""))',
    'p': 'y, x = stack.pop(2); stack.push(int(str(x).startswith(str(y)))',
    'q': 'stack.push('"' + str(stack.pop()) + '"')',
    'r': 'lhs, rhs = stack.pop(2); stack.push(list(orderless_range(rhs, lhs)))',
    's': 'top = stack.pop(); stack.push(sorted(as_iter(top)))',
    't': 'stack.push(as_iter(stack.pop())[-1])',
    'u': 'TODO',
    'w': 'stack.push(Stack([stack.pop()]))',
    'x': '_context_level -= 1 * (1 - (_context_level == 0))',
    'y': 'TODO',
    'z': 'TODO',
    '~': 'stack.push(random.randint(-INT, INT))',
    '¬': 'stack.push(not stack.pop())',
    '∧': 'lhs, rhs = stack.pop(2); stack.push(bool(rhs and lhs))',
    '⟑': 'lhs, rhs = stack.pop(2); stack.push(rhs and lhs)',
    '∨': 'lhs, rhs = stack.pop(2); stack.push(bool(rhs or lhs))',
    '⟇': 'lhs, rhs = stack.pop(2); stack.push(rhs or lhs)',
    '÷': 'for item in as_iter(stack.pop()): stack.push(item)',
    '⍎': 'fn = stack.pop(); stack += fn(stack) if fn.fn_type == STANDARD else Stack(fn(stack.pop()))',
    'Ṛ': 'lhs, rhs = stack.pop(2); stack.push(random.randint(rhs, lhs))',
    'Ï': 'lhs, rhs = stack.pop(2); stack.push(as_iter(rhs).index(lhs))',
    'Ô': 'TODO',
    'Ç': 'TODO',
    'ʀ': 'stack.push(Stack(list(range(0, stack.pop() + 1))))',
    'ʁ': 'stack.push(Stack(list(range(0, stack.pop()))))',
    'ɾ': 'stack.push(Stack(list(range(1, stack.pop() + 1))))',
    'ɽ': 'stack.push(Stack(list(range(1, stack.pop()))))',
    'Þ': 'top = as_iter(stack.pop()); stack.push(top == top[::-1])',
    'ƈ': 'TODO',
    '∞': 'TODO',
    'ß': 'TODO',
    "ř": "lhs, rhs = stack.pop(2); stack.push(rhs * lhs)",
    '∺': 'stack.push(stack.pop() % 2)',
    "∻": 'lhs, rhs = stack.pop(2); stack.push(int((rhs % lhs) == 0))',
    '\n': '',
    '\t': '',
    "Ĥ": "stack.push(100)",
    "Ĵ": "stack.push(''.join(stack.pop())",
    "Ĳ": "stack.push('\\n'.join(stack.pop()))",
    "ĳ": "stack.push(10)",
    "ĵ": "x = stack.pop(); stack.push(x * x)",
    "∑": "stack.push(summate(stack.pop()))",
    "Ķ": "rhs, lhs = stack.pop(2); stack.push(Stack([lhs, rhs]))",
    "č": "stack.push(int(stack.pop() != 1))",
    "½": "stack.push(divide(stack.pop(), 2))",
    "⨪": "stack.push(subtract(stack.pop(), 1))",
    "⨥": "stack.push(add(stack.pop(), 1))",
    "ķ": "rhs, lhs = stack.pop(2); stack.push(list(orderless_range(lhs, rhs, 1)))",
    "ṙ": "stack.push(VyRound(stack.pop()))",
    "√": "stack.push(stack.pop() ** (1 / 2))",
    "∖": "rhs, lhs = stack.pop(2); stack.push(lhs // rhs)",
    "Ẋ": "rhs, lhs = stack.pop(2); stack.push(int((a or b) and not (a and b)))",
    "Ȧ": "stack.push(abs(stack.pop()))",
    "Ȯ": "stack.push(oct(stack.pop()))",
    "ĸ": "value, iterable = stack.pop(2); stack.push(distribute(iterable, value))",
    "Ĺ": "stack.push('\n')",
    "ĺ": "stack.push(vertical_join(stack.pop()))",
    "Ļ": "padding, iterable = stack.pop(2); stack.push(vertical_join(iterable, padding))",
    "Ń": "n, fn = stack.pop(2); stack.do_fixed_gen(fn, n)",
    "ń": "stack.do_fixed_gen(stack.pop())",
    "Ň": "stack.push(math.factorial(stack.pop()))",
    "ņ": "stack.push(sums(as_iter(stack.pop())))",
    "Ň": "stack.push(int(len(set(as_iter(stack.pop()))) == 1))",
    "ð": "stack.push(' ')"
    }
