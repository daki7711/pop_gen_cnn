import numpy as np

u = np.load('final.split.up.seln.big.npz', encoding = 'latin1', allow_pickle=True)


np.savez_compressed('final.split.up.seln.small.npz', xfinal=u['xfinal'], yfinal=u['yfinal'], posfinal=u['posfinal'], 
													  xtest=u['xtest'], ytest=u['ytest'], postest=u['postest'],
                                                      postrain_0=u['postrain_0'], xtrain_0= u['xtrain_0'], ytrain_0= u['ytrain_0'],
                                                      postrain_3000=u['postrain_3000'], xtrain_3000= u['xtrain_3000'], ytrain_3000=u['ytrain_3000'],
                                                      postrain_171000=u['postrain_171000'], xtrain_171000= u['xtrain_171000'], ytrain_171000=u['ytrain_171000'],
                                                      postrain_195000=u['postrain_195000'], xtrain_195000= u['xtrain_195000'], ytrain_195000=u['ytrain_195000'],
                                                      postrain_228000=u['postrain_228000'], xtrain_228000= u['xtrain_228000'], ytrain_228000=u['ytrain_228000'])
