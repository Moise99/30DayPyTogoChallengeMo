# 1. 

class Statistics:
    def __init__(self, data):
        self.data = data
        self.count = len(data)

    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    def max(self):
        return max(self.data)
    def range(self):
        return self.max() - self.min()
    def mean(self):
        return round(self.sum() / self.count)
    def median(self):
        sorted_data = sorted(self.data)
        mid = self.count // 2
        if self.count % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]
    def mode(self):
        from collections import Counter
        data_count = Counter(self.data)
        mode_data = data_count.most_common(1)[0]
        return {'mode': mode_data[0], 'count': mode_data[1]}
    def std(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / self.count
        return round(variance ** 0.5, 1)
    def var(self):
        mean = self.mean()
        return round(sum((x - mean) ** 2 for x in self.data) / self.count, 1)
    def freq_dist(self):
        from collections import Counter
        data_count = Counter(self.data)
        total_count = sum(data_count.values())
        freq_distribution = [(count / total_count * 100, value) for value, count in data_count.items()]
        return sorted(freq_distribution, reverse=True)
    def describe(self):
        return {
            'Count': self.count,
            'Sum': self.sum(),
            'Min': self.min(),
            'Max': self.max(),
            'Range': self.range(),
            'Mean': self.mean(),
            'Median': self.median(),
            'Mode': self.mode(),
            'Variance': self.var(),
            'Standard Deviation': self.std(),
            'Frequency Distribution': self.freq_dist()
        }
    def __str__(self):
        description = self.describe()
        output = []
        for key, value in description.items():
            if isinstance(value, dict):
                output.append(f"{key}: ({value['mode']}, {value['count']})")
            elif isinstance(value, list):
                output.append(f"{key}: {value}")
            else:
                output.append(f"{key}: {value}")
        return "\n".join(output)
# Example usage
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
        33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data)
# Output will be printed in the format specified in the prompt
# The output will be printed in the format specified in the prompt