class Vocab:
    def __init__(self, vocab_file, max_size=13541):
        """Creates a vocab of up to max_size words, reading from the vocab_file. If max_size is 0, reads the entire vocab file.

            Args:
              vocab_file: path to the vocab file, which is assumed to contain "<word> <frequency>" on each line, sorted with most frequent word first. This code doesn't actually use the frequencies, though.
              max_size: integer. The maximum size of the resulting Vocabulary."""
        self.word2id = {}
        self.id2word = {}
        self.count = 0

        with open(vocab_file, 'r', encoding='utf-8') as f:
            for line in f:
                pieces = line.split()
                if len(pieces) != 2:
                    print('Warning : incorrectly formatted line in vocabulary file : %s\n' % line)
                    continue

                w = pieces[0]

                if w in self.word2id:
                    raise Exception('Duplicated word in vocabulary file: %s' % w)

                self.word2id[w] = self.count
                self.id2word[self.count] = w
                self.count += 1
                if max_size != 0 and self.count >= max_size:
                    print("max_size of vocab was specified as %i; we now have %i words. Stopping reading." % (
                    max_size, self.count))
                    break

        print("Finished constructing vocabulary of %i total words. Last word added: %s" % (
        self.count, self.id2word[self.count - 1]))

    def word_to_id(self, word):
        if word not in self.word2id:
            raise ValueError('Id not found in vocab: %s' % word)
        return self.word2id[word]

    def id_to_word(self, word_id):
        if word_id not in self.id2word:
            raise ValueError('Id not found in vocab: %d' % word_id)
        return self.id2word[word_id]

    def size(self):
        return self.count