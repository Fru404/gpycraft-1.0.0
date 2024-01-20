import re

class dotstacks:
    def __init__(self):
        self.before_dot_stack = []
        self.after_dot_stack = []

    def process_text(self, text):
        # Use regular expression to capture entire lines before and after dots
        pattern = re.compile(r'(.+?)\s*\.(.*)')
        matches = pattern.findall(text)

        # Iterate through the matches and populate the stacks
        for before, after in matches:
            self.before_dot_stack.append(before.strip())
            self.after_dot_stack.append(after.strip())

    def display_stacks(self):
        #print("Before Dot Stack:", self.before_dot_stack)
        #print("After Dot Stack:", self.after_dot_stack)
        
        return self.before_dot_stack
