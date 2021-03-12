from II_syntactic.node_types import ASTNodeType


class Interpreter:
    def __init__(self):
        self.interpret = {
            ASTNodeType.ASS_STMT: self.interpret_assignment_statement,
            ASTNodeType.EXP_STMT: self.interpret_expression_statement,
            ASTNodeType.CLR_STMT: self.interpret_clear_statement,
        }
        self.evaluate = {
            ASTNodeType.LOR_EXP: self.evaluate_logic_or_expression,
            ASTNodeType.LAN_EXP: self.evaluate_logic_and_expression,
            ASTNodeType.EQL_EXP: self.evaluate_equal_expression,
            ASTNodeType.REL_EXP: self.evaluate_relational_expression,
            ASTNodeType.ADD_EXP: self.evaluate_additive_expression,
            ASTNodeType.MUL_EXP: self.evaluate_multiplicative_expression,
            ASTNodeType.UNY_EXP: self.evaluate_unary_expression,
            ASTNodeType.PRI_EXP: self.evaluate_primary_expression,
            ASTNodeType.NUM_LIT: self.evaluate_number_literal,
            ASTNodeType.STR_LIT: self.evaluate_string_literal,
            ASTNodeType.ID: self.evaluate_identifier,
        }
        self.variables = {}

    def interpret_program(self, root):
        for child in root.get_children():
            self.interpret_statement(child)

    def interpret_statement(self, node):
        result = self.interpret[node.get_type()](node)
        # if statement does not ended with a semicolon, the result is printed
        if result:
            var = result[0]
            value = result[1]
            if isinstance(value, float):
                if int(value) == value:
                    print(f"\n{var} =\n\n     {int(value)}\n")
                else:
                    print(f"\n{var} =\n\n     {value:.4f}\n")
            else:
                print(f"\n{var} =\n\n     {value}\n")

    def interpret_assignment_statement(self, node):
        var_name = node.get_text()
        child = node.get_child(0)
        if var_name not in self.variables:
            # to adapt the dynamic type feature in interpreted language,
            # assignment could have the same form as declaration
            # because the type specifiers are omitted.
            # which means that assigning to an nonexistent variable is allowed since it is declaration
            pass
        self.variables[var_name] = self.evaluate[child.get_type()](child)

        return (var_name, self.variables[var_name]) if node.num_children() == 1 else None

    def interpret_expression_statement(self, node):
        var_name = "ans"
        child = node.get_child(0)
        # ans stored as a temporary variable
        self.variables[var_name] = self.evaluate[child.get_type()](child)

        return (var_name, self.variables[var_name]) if node.num_children() == 1 else None

    def interpret_clear_statement(self, node):
        variables = [child.get_text() for child in node.get_children()]
        self.del_variables(var_list=variables if variables else None)

    def evaluate_logic_or_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        return 1 if self.evaluate[child0.get_type()](child0) or self.evaluate[child1.get_type()](child1) else 0

    def evaluate_logic_and_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        return 1 if self.evaluate[child0.get_type()](child0) and self.evaluate[child1.get_type()](child1) else 0

    def evaluate_equal_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        if node.get_text() == "==":
            return 1 if self.evaluate[child0.get_type()](child0) == self.evaluate[child1.get_type()](child1) else 0
        else:
            return 1 if self.evaluate[child0.get_type()](child0) != self.evaluate[child1.get_type()](child1) else 0

    def evaluate_relational_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        if node.get_text() == ">=":
            return 1 if self.evaluate[child0.get_type()](child0) >= self.evaluate[child1.get_type()](child1) else 0
        elif node.get_text() == ">":
            return 1 if self.evaluate[child0.get_type()](child0) > self.evaluate[child1.get_type()](child1) else 0
        elif node.get_text() == "<=":
            return 1 if self.evaluate[child0.get_type()](child0) <= self.evaluate[child1.get_type()](child1) else 0
        else:
            return 1 if self.evaluate[child0.get_type()](child0) < self.evaluate[child1.get_type()](child1) else 0

    def evaluate_additive_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        if node.get_text() == "+":
            return self.evaluate[child0.get_type()](child0) + self.evaluate[child1.get_type()](child1)
        else:
            return self.evaluate[child0.get_type()](child0) - self.evaluate[child1.get_type()](child1)

    def evaluate_multiplicative_expression(self, node):
        child0 = node.get_child(0)
        child1 = node.get_child(1)
        if node.get_text() == "*":
            return self.evaluate[child0.get_type()](child0) * self.evaluate[child1.get_type()](child1)
        else:
            return self.evaluate[child0.get_type()](child0) / self.evaluate[child1.get_type()](child1)

    def evaluate_unary_expression(self, node):
        child = node.get_child()
        if node.get_text() == "+":
            return self.evaluate[child.get_type()](child)
        elif node.get_text() == "-":
            return -self.evaluate[child.get_type()](child)
        else:
            return 0 if self.evaluate[child.get_type()](child) else 1

    def evaluate_primary_expression(self, node):
        # will not be used since in AST it is optimised to skip single-child node
        pass

    @staticmethod
    def evaluate_number_literal(node):
        """
        By default, MATLAB® stores all numeric variables as double-precision floating-point values.
        """
        return float(node.get_text())

    @staticmethod
    def evaluate_string_literal(node):
        return node.get_text()

    def evaluate_identifier(self, node):
        var_name = node.get_text()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            # todo: raise unknown exception variable exception
            pass

    def get_variables(self):
        return self.variables

    def del_variables(self, var_list=None):
        if var_list:
            for var in var_list:
                # todo: check exist and raise error
                del self.variables[var]
        else:
            self.variables = {}
