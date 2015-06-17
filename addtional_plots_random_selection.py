import random
plots = Plot.objects.filter(selected=2, replaces__isnull=True, replaced_by__isnull=True, action='unconfirmed')
sample_size = 41
rand_smpl = [ plots[i] for i in sorted(random.sample(xrange(len(plots)), sample_size)) ]
ids = []
for p in rand_smpl:
    ids.append(p.plot_identifier)
