import numpy as np

u = np.load('final.split.up.seln.big.npz', encoding = 'latin1', allow_pickle=True)


np.savez_compressed('final.split.up.seln.small.npz', xfinal=u['xfinal'], yfinal=u['yfinal'], posfinal=u['posfinal'], 
													  xtest=u['xtest'], ytest=u['ytest'], postest=u['postest'],
                                                      postrain_18000=u['postrain_18000'], xtrain_18000= u['xtrain_18000'], ytrain_18000= u['ytrain_18000'],
                                                      postrain_57000=u['postrain_57000'], xtrain_57000= u['xtrain_57000'], ytrain_3000=u['ytrain_57000'],
                                                      postrain_108000=u['postrain_108000'], xtrain_108000= u['xtrain_108000'], ytrain_108000=u['ytrain_108000'],
                                                      postrain_135000=u['postrain_135000'], xtrain_135000= u['xtrain_135000'], ytrain_135000=u['ytrain_135000'],
                                                      postrain_171000=u['postrain_171000'], xtrain_171000= u['xtrain_171000'], ytrain_171000=u['ytrain_171000'],
                                                      postrain_195000=u['postrain_195000'], xtrain_195000= u['xtrain_195000'], ytrain_195000=u['ytrain_195000'],
                                                      postrain_231000=u['postrain_231000'], xtrain_231000= u['xtrain_231000'], ytrain_231000=u['ytrain_231000'])
