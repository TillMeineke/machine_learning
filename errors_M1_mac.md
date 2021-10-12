# Errors using MacBook Pro(13-inch, M1 , 2020)

can´t load data

kernel scheint abzustürzen

# Errors trying to install software on MacBook Pro(13-inch, M1 , 2020) 

### tried to install mediapipe with:


### tried to install xgboost with:

1. `conda install xgboost`
2. `pip install xgboost`

both failed with errors

### tried to install geopandas with:

1. `conda install geopandas`

-> error

2. `pip install geopandas`

error (but all in red and yello):

```
nd errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpxsyqhr1p Check the logs for full command output.
  Downloading pyproj-2.4.1.tar.gz (462 kB)
     |████████████████████████████████| 462 kB 7.5 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp7wj38ldo
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_dc9b56240dd14f3e92e956271fe664df
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/8c/7e/c34acb5abca1916ba0a294df4a90935d6d1cfc446ad1c076986bbf0118d3/pyproj-2.4.1.tar.gz#sha256=817d4b762adee4479200471042e2393f75a8ec2384061979ccfe177b862b4f8b (from https://pypi.org/simple/pyproj/) (requires-python:>=3.5). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp7wj38ldo Check the logs for full command output.
  Downloading pyproj-2.4.0.tar.gz (460 kB)
     |████████████████████████████████| 460 kB 8.4 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpf0cxnug0
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_e0c9f906fce441888c4757f180740e80
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/f6/16/bda05734b5a54060040aba5aefadae896829aab8ff02db11bad967d5bc61/pyproj-2.4.0.tar.gz#sha256=8124fe43d81a7caca43df6930110e2bfd2bd3b82b86587eefd6f6d86a81a658e (from https://pypi.org/simple/pyproj/) (requires-python:>=3.5). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpf0cxnug0 Check the logs for full command output.
  Downloading pyproj-2.3.1.tar.gz (422 kB)
     |████████████████████████████████| 422 kB 7.8 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp88u21gfp
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_85f72dbfeab141be97d8cbdbffc5b603
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/5e/57/e6bc86f9d407e87db4c859590f799bbffb455940783ea3629b3771619c79/pyproj-2.3.1.tar.gz#sha256=92b8cf0703c25f4e197ec8696b1be567ebb33cb8ba542956142a61df6bf1b766 (from https://pypi.org/simple/pyproj/) (requires-python:>=3.5). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp88u21gfp Check the logs for full command output.
  Downloading pyproj-2.3.0.tar.gz (415 kB)
     |████████████████████████████████| 415 kB 7.7 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp8_ncfpyd
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_251b3ef6b82a4793bdac4ddf44dc01c9
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/49/94/06c20b7f65a0efc31da7c734ea4c9385a3b26e5aec619a5b83383dffed93/pyproj-2.3.0.tar.gz#sha256=9c50988827076c685ebaf384b7a6993e193c026aad181b6a579f5a3f6915a37d (from https://pypi.org/simple/pyproj/) (requires-python:>=3.5). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp8_ncfpyd Check the logs for full command output.
  Downloading pyproj-2.2.2.tar.gz (7.2 MB)
     |████████████████████████████████| 7.2 MB 6.8 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpdy3q_6je
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_d7a34a9026354cb49f5215ae8455ed6f
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/f5/79/ceb215614d5673ff482a85217499f0030d9a5e2b2a8c68ac32b16df35f97/pyproj-2.2.2.tar.gz#sha256=6f129a00afdd817dbb331af5709221f35012bcc11a23b8c83fa09197c1190786 (from https://pypi.org/simple/pyproj/). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpdy3q_6je Check the logs for full command output.
  Downloading pyproj-2.2.1.tar.gz (382 kB)
     |████████████████████████████████| 382 kB 6.8 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpo4f79eyn
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_a3f812fad66345838fbb91137846c2ed
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/7d/41/f0c8e63d20cd56596bfd88a455738629734faa26f26bbdf4d301330748ad/pyproj-2.2.1.tar.gz#sha256=ec89e68a0cf210af0cc2724b5f8601d4b6809ff0f556e16efc8c955e79672f7a (from https://pypi.org/simple/pyproj/). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpo4f79eyn Check the logs for full command output.
  Downloading pyproj-2.2.0.tar.gz (378 kB)
     |████████████████████████████████| 378 kB 8.3 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp9a5rxy7y
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_2c5cd0c1a6154013a0b9b7e358977a6f
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/73/ef/53a7e9e98595baf4d7212aa731fcec256b432a3db60a55b58a027a4d9d47/pyproj-2.2.0.tar.gz#sha256=0a4f793cc93539c2292638c498e24422a2ec4b25cb47545addea07724b2a56e5 (from https://pypi.org/simple/pyproj/). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp9a5rxy7y Check the logs for full command output.
Collecting geopandas
  Downloading geopandas-0.8.2-py2.py3-none-any.whl (962 kB)
     |████████████████████████████████| 962 kB 7.6 MB/s 
  Downloading geopandas-0.8.1-py2.py3-none-any.whl (962 kB)
     |████████████████████████████████| 962 kB 7.8 MB/s 
  Downloading geopandas-0.8.0-py2.py3-none-any.whl (962 kB)
     |████████████████████████████████| 962 kB 7.9 MB/s 
  Downloading geopandas-0.7.0-py2.py3-none-any.whl (928 kB)
     |████████████████████████████████| 928 kB 6.5 MB/s 
  Downloading geopandas-0.6.3-py2.py3-none-any.whl (920 kB)
     |████████████████████████████████| 920 kB 8.0 MB/s 
Collecting pyproj
  Downloading pyproj-2.1.3.tar.gz (521 kB)
     |████████████████████████████████| 521 kB 6.6 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp252nf6_n
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_44521cd22d3e4f9ea5bdc23e43b35ea2
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/a5/05/edfcfd0752e1e3fe5e06245863412bb9aa77888143f6c8900dea62aecdc2/pyproj-2.1.3.tar.gz#sha256=99c52788b01a7bb9a88024bf4d40965c0a66a93d654600b5deacf644775f424d (from https://pypi.org/simple/pyproj/). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp252nf6_n Check the logs for full command output.
  Downloading pyproj-2.1.2.tar.gz (492 kB)
     |████████████████████████████████| 492 kB 8.0 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpd0rk35_b
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_be75d4d5859d4f82a610d82bd7eeb5f1
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/7f/d9/62db3608c734fdd02cb5113a89f377a8b012d14beaee6525afc029b590d4/pyproj-2.1.2.tar.gz#sha256=fe1a50be22151ed9798e993c35b58305fe71d03242afc45ff79570e3fa0312e7 (from https://pypi.org/simple/pyproj/). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpd0rk35_b Check the logs for full command output.
  Downloading pyproj-2.1.1.tar.gz (461 kB)
     |████████████████████████████████| 461 kB 8.7 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpuy54ib6f
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_59137a0c78704ad0b2cbf92ca3b2703d
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/1c/64/85bd290cd79dc59a8d2a012bbde3091cc6e8bc8d4b025b419e675315cb71/pyproj-2.1.1.tar.gz#sha256=ac6176ba67e9184bb77748f2b31650d9a72ddf45beb1575555abe8160935964d (from https://pypi.org/simple/pyproj/). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpuy54ib6f Check the logs for full command output.
  Downloading pyproj-2.1.0.tar.gz (459 kB)
     |████████████████████████████████| 459 kB 7.6 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp_1xf1z6l
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_40803e7e032b45538a212d162c40124e
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/20/20/73550cc254ffc6168b3890ece3642514cc176b2ec342f08ed695376b4aca/pyproj-2.1.0.tar.gz#sha256=40d9d6ec9b53c1edabe88bc376e7cd2d1cdd3b338be4485390f086f412e4ac7d (from https://pypi.org/simple/pyproj/). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmp_1xf1z6l Check the logs for full command output.
  Downloading pyproj-2.0.2.tar.gz (407 kB)
     |████████████████████████████████| 407 kB 6.4 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpbfv2_pzs
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_f17c11101f4a4394bb41ce5b6ebb3c4f
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/ea/58/7f28e5aed3538d589e56af564892ff1f5ed5519cff6a1d0ed852b97870df/pyproj-2.0.2.tar.gz#sha256=d9c5cc3df26bfc0fdc27fd70b4fe3475e3c224326fdf53dfd5b7bef1b87f1780 (from https://pypi.org/simple/pyproj/). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpbfv2_pzs Check the logs for full command output.
  Downloading pyproj-2.0.1.tar.gz (408 kB)
     |████████████████████████████████| 408 kB 7.7 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmphc8mdrq1
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_104ef2cd98a24ae39a5dbaeb1b973631
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/65/ad/c1367acde6a0a8f5513f8d9fd11d7417cfdc7702caccb483a575be86d87d/pyproj-2.0.1.tar.gz#sha256=f2ac42ee0bf52cd4320c7e2d6793fa7e6a4901612a9e85194590ecf885035e56 (from https://pypi.org/simple/pyproj/). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmphc8mdrq1 Check the logs for full command output.
  Downloading pyproj-2.0.0.tar.gz (408 kB)
     |████████████████████████████████| 408 kB 7.8 MB/s 
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpcx7x5sha
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/pyproj_e21fbd549bee4666ba329023e1a7d1e1
  Complete output (1 lines):
  Proj executable not found. Please set PROJ_DIR variable.
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/53/4b/21643a93e7d33941498087290636e34c6d534aa8baa1ada54cf0d096ffaa/pyproj-2.0.0.tar.gz#sha256=aa8f0fda988353f37831356d82aadafa4b44815d3c4daadcda046f0f345567ce (from https://pypi.org/simple/pyproj/). Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages/pip/_vendor/pep517/in_process/_in_process.py get_requires_for_build_wheel /var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/tmpcx7x5sha Check the logs for full command output.
  Downloading pyproj-1.9.6.tar.gz (2.8 MB)
     |████████████████████████████████| 2.8 MB 8.4 MB/s 
Collecting shapely
  Downloading Shapely-1.7.1.tar.gz (383 kB)
     |████████████████████████████████| 383 kB 7.5 MB/s 
Requirement already satisfied: pandas>=0.23.0 in /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages (from geopandas) (1.3.3)
Collecting fiona
  Downloading Fiona-1.8.20.tar.gz (1.3 MB)
     |████████████████████████████████| 1.3 MB 7.8 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_8257360ce3fd43b8b6ed081248ea19d6/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_8257360ce3fd43b8b6ed081248ea19d6/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-1n5lkqb0
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_8257360ce3fd43b8b6ed081248ea19d6/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/ec/f7/093890341a7e8fbfcdfa04caf4dfb588ebab32c13ceaa6a3819da79ea106/Fiona-1.8.20.tar.gz#sha256=a70502d2857b82f749c09cb0dea3726787747933a2a1599b5ab787d74e3c143b (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.19.tar.gz (1.3 MB)
     |████████████████████████████████| 1.3 MB 7.4 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_478e06760b584d33acd5d2ee4739cae2/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_478e06760b584d33acd5d2ee4739cae2/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-44zvtnl7
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_478e06760b584d33acd5d2ee4739cae2/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/a0/d9/6042aeb073d11341f7726de0586ff71c13117c34959dcf07bd4ee6d4b93e/Fiona-1.8.19.tar.gz#sha256=b9059e0b29c2e9e6b817e53f941e77e1aca7075f986005d38db307067b60458f (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.18.tar.gz (1.3 MB)
     |████████████████████████████████| 1.3 MB 8.0 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_d946b86c69fc4956aaa2d8d46ee9c8e9/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_d946b86c69fc4956aaa2d8d46ee9c8e9/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-crw6z8b8
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_d946b86c69fc4956aaa2d8d46ee9c8e9/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/9f/e8/401cdaa58d862a25c4b3365acf7d2bd7ac77191e3dc9acdcdac0eff20ff0/Fiona-1.8.18.tar.gz#sha256=b732ece0ff8886a29c439723a3e1fc382718804bb057519d537a81308854967a (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.17.tar.gz (1.3 MB)
     |████████████████████████████████| 1.3 MB 7.9 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_31ff7af8f1b745778d25ba964b3afe3f/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_31ff7af8f1b745778d25ba964b3afe3f/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-8xdmrub9
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_31ff7af8f1b745778d25ba964b3afe3f/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/88/62/69347ba2c41b526e1953c4cb66d51170b2869808863c03af202ba0121670/Fiona-1.8.17.tar.gz#sha256=716201c21246587f374785bec6d6a20a984fe1f6c2b0e83bf15127eb8f724d0c (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.16.tar.gz (1.3 MB)
     |████████████████████████████████| 1.3 MB 7.7 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_c3b8e7f116c74d17bde1122dd8355df3/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_c3b8e7f116c74d17bde1122dd8355df3/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-v34c84ib
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_c3b8e7f116c74d17bde1122dd8355df3/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/1e/60/dfc6115a11338d8aa96cacd8c60635223d9c97d61d556c90acc5dfd663fa/Fiona-1.8.16.tar.gz#sha256=fd6dfb65959becc916e9f6928618bfd59c16cdbc413ece0fbac61489cd11255f (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.15.tar.gz (1.3 MB)
     |████████████████████████████████| 1.3 MB 6.4 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_01e3a7b946a34392b38a584077286d91/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_01e3a7b946a34392b38a584077286d91/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-6a8tkg7b
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_01e3a7b946a34392b38a584077286d91/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/55/2f/17450ec2c8fcc720a8a3e4d9a383499508475c7cfb90f7eca9fb585ac598/Fiona-1.8.15.tar.gz#sha256=3b1c9b5c834fae2fe947cfaea176db890bc6750d1a6ba9f54d969c19ffcd191e (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.14.tar.gz (1.3 MB)
     |████████████████████████████████| 1.3 MB 8.3 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_1bacb807f654496aab3b2fc45622a48d/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_1bacb807f654496aab3b2fc45622a48d/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-wya9be4a
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_1bacb807f654496aab3b2fc45622a48d/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/5c/fd/5ec54f2d9b3d5dd23dd443fad5630d6b872e2664814c68b856c47e0d65af/Fiona-1.8.14.tar.gz#sha256=6eac038206c89d2cf5f99ea38b81cc228dc21eac5f47870a9a32d453b0007f4d (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.13.post1.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 8.2 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_29b46f32294944158898f0c4d86f6338/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_29b46f32294944158898f0c4d86f6338/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-h4pm44rh
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_29b46f32294944158898f0c4d86f6338/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/6d/42/f4a7cac53b28fa70e9a93d0e89a24d33e14826dad6644b699362ad84dde0/Fiona-1.8.13.post1.tar.gz#sha256=1a432bf9fd56f089256c010da009c90d4a795c531a848132c965052185336600 (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.13.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 8.0 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_8cb29276e2c2479fb8090b0cd212ffce/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_8cb29276e2c2479fb8090b0cd212ffce/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-dgtlenaa
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_8cb29276e2c2479fb8090b0cd212ffce/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/be/04/31d0a6f03943b1684f32c9b861be40c1fd282468fa6bd54ddf4a774e6b0f/Fiona-1.8.13.tar.gz#sha256=5ec34898c8b983a723fb4e949dd3e0ed7e691c303e51f6bfd61e52ac9ac813ae (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.12.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 7.5 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_ade3ebfea47c48a5a453688a9c0fe0e8/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_ade3ebfea47c48a5a453688a9c0fe0e8/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-jz65ppit
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_ade3ebfea47c48a5a453688a9c0fe0e8/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/97/d8/feab39987296437fbdc3029fb39752a14355d217d73b93471010b8dd63a3/Fiona-1.8.12.tar.gz#sha256=c9266ddf6ae2a64fcea20014ddf27f800ac07584f2fdb09c2a02f3b3a52e371c (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.11.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 7.2 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_41955384166c4085be05492edda44103/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_41955384166c4085be05492edda44103/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-no8o_02p
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_41955384166c4085be05492edda44103/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/9d/f4/0a0ddc6174c4a93679b5f1dd3535e7ef8989828e6d5f86112de681f8c87b/Fiona-1.8.11.tar.gz#sha256=1e7ca9e051f5bffa1c43c70d573da9ca223fc076b84fa73380614fc02b9eb7f6 (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.10.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 8.4 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_1cdf42a264984886a63c05cd024eae24/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_1cdf42a264984886a63c05cd024eae24/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-kf4a7553
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_1cdf42a264984886a63c05cd024eae24/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/13/73/f80b491ed8559326fab202a6d6333a3cd6e8be1e9d782bc6c0d03d476457/Fiona-1.8.10.tar.gz#sha256=ff562eb2f3960e21f8c7f050ddd7f47a763869ea14afc2234a40df72666c6a2c (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.9.post2.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 7.0 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_76dc5c0e726347e6b4368cf3b35596d2/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_76dc5c0e726347e6b4368cf3b35596d2/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-71tpa1_r
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_76dc5c0e726347e6b4368cf3b35596d2/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/9b/52/45e75507660ce0e86176d0f59b659560f687e2c7e9ebf82a10e7dcd2d3b7/Fiona-1.8.9.post2.tar.gz#sha256=210fb038b579fab38f35ddbdd31b9725f4d5099b3edfd4b87c983e5d47b79983 (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.9.post1.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 8.4 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_4117bdfeb0eb46efb8bc066efc15511a/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_4117bdfeb0eb46efb8bc066efc15511a/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-9gzalwyl
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_4117bdfeb0eb46efb8bc066efc15511a/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/0e/a4/d9dd7399be809d3990f5000fb6ae43189ea26ae88be1bed3a4c9ddc1becc/Fiona-1.8.9.post1.tar.gz#sha256=d5e0ea0b8addffe9cba4cb59e2bd495b015230e7a1b1597974f5048211930199 (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.9.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 8.0 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_ff7f14778ef0419c849a80ab450726eb/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_ff7f14778ef0419c849a80ab450726eb/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-t9yge4fu
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_ff7f14778ef0419c849a80ab450726eb/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/ad/92/dcbd8c54d697c22f299b5af63b6df3acfbd06c6d72e249614c05be99337c/Fiona-1.8.9.tar.gz#sha256=4dd6e2f5327c1174143c7c8594a75d373bc72f2c9a2a6daee312c3186a128add (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.8.tar.gz (1.7 MB)
     |████████████████████████████████| 1.7 MB 7.8 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_e49da5a69f5b45e48c5c8e7ef34c4d01/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_e49da5a69f5b45e48c5c8e7ef34c4d01/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-nf90afqd
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_e49da5a69f5b45e48c5c8e7ef34c4d01/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/94/7f/e288db1ad63d759d494c30caae34f865e0c6927588c490705e91b7134193/Fiona-1.8.8.tar.gz#sha256=711c3be73203b37812992089445a1e4e9d3d6b64e667389f7b15406e15a91e83 (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.7.tar.gz (1.7 MB)
     |████████████████████████████████| 1.7 MB 8.2 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_84e49233c6fd499eb7093d48f4be29a7/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_84e49233c6fd499eb7093d48f4be29a7/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-zxo8yh03
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_84e49233c6fd499eb7093d48f4be29a7/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/78/62/daafd070aebefa639df247705b97f13f7cfad43895581b5cae41bd886709/Fiona-1.8.7.tar.gz#sha256=a55a23615bad3e142d4e4cda97bb5de83c778a80049222e9dffae93c13b5cf93 (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.6.tar.gz (1.7 MB)
     |████████████████████████████████| 1.7 MB 6.6 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_c2458bb038cb4a789cdee3806b5926ed/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_c2458bb038cb4a789cdee3806b5926ed/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-im7oc7tc
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_c2458bb038cb4a789cdee3806b5926ed/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/41/9d/63696e7b1de42aad294d4781199a408bec593d8fdb80a2b4a788c911a33b/Fiona-1.8.6.tar.gz#sha256=fa31dfe8855b9cd0b128b47a4df558f1b8eda90d2181bff1dd9854e5556efb3e (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.5.tar.gz (1.7 MB)
     |████████████████████████████████| 1.7 MB 9.3 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_2132891813764cb1bae10b9123768827/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_2132891813764cb1bae10b9123768827/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-7e8h19gj
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_2132891813764cb1bae10b9123768827/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/7b/af/1c2c83c4a8363a4ce9fea817b1910b5e071bed012e18257faa2a0ab3cfe7/Fiona-1.8.5.tar.gz#sha256=4f5cc2d449edbbf693c83e24cdada72de7c41297383d16fcc92387eb445e9d35 (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.4.tar.gz (1.1 MB)
     |████████████████████████████████| 1.1 MB 7.7 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_07bc858a6c7f43faba5712bcfaf84f21/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_07bc858a6c7f43faba5712bcfaf84f21/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-751kkf7_
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_07bc858a6c7f43faba5712bcfaf84f21/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/3a/16/84960540e9fce61d767fd2f0f1d95f4c63e99ab5d8fddc308e8b51b059b8/Fiona-1.8.4.tar.gz#sha256=aec9ab2e3513c9503ec123b1a8573bee55fc6a66e2ac07088c3376bf6738a424 (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.3.tar.gz (1.1 MB)
     |████████████████████████████████| 1.1 MB 7.6 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_8567e5c8c44a4922b5905b6211ea116a/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_8567e5c8c44a4922b5905b6211ea116a/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-y9puahx8
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_8567e5c8c44a4922b5905b6211ea116a/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/46/d1/fcdb32513a03abfde0d97fd9782ce0f8cc0540fa6c6ce783e87b94064964/Fiona-1.8.3.tar.gz#sha256=3e831100a23c3b6cd32b98baf0c9e2119d909b44a5cf4533d3625f61dcf2d2b1 (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.2.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 7.0 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_26fd1f36ab534afcaaae677dfed3e440/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_26fd1f36ab534afcaaae677dfed3e440/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-w8oe12s4
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_26fd1f36ab534afcaaae677dfed3e440/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/25/50/0466d5d83e1859c5ca38351ee932d64cc5635f9d4dad522879e58f4b0018/Fiona-1.8.2.tar.gz#sha256=4c6419b7ac29136708029f6a44b4ccd458735a4d241016c7b1bab41685c08d8f (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.1.tar.gz (1.1 MB)
     |████████████████████████████████| 1.1 MB 7.1 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_850199843bd146d6982f8ce99e656541/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_850199843bd146d6982f8ce99e656541/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-j07uebe8
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_850199843bd146d6982f8ce99e656541/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/3e/5f/0c6704efeea2ff3fba7f54cc6ec38070157f21bc1cffa7bdfa7c9f6b8f7a/Fiona-1.8.1.tar.gz#sha256=4c34bb4c5cd788aaf14e5484c3b7de407b1a8a7c7b2d29bbb2e8b37931e83b8d (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.8.0.tar.gz (1.4 MB)
     |████████████████████████████████| 1.4 MB 7.6 MB/s 
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_f0015763c14343c396a53d97433165b0/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_f0015763c14343c396a53d97433165b0/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-pip-egg-info-blbubsc5
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_f0015763c14343c396a53d97433165b0/
    Complete output (2 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/2a/bd/c1efc2680f338e5941121c776d6323af6b9698ac739e22ba523cee348a7f/Fiona-1.8.0.tar.gz#sha256=20141a9ece06daa7bb4333fba640c2fe39a49f8aca5492d1da8595d41e91844a (from https://pypi.org/simple/fiona/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  Downloading Fiona-1.7.13.tar.gz (731 kB)
     |████████████████████████████████| 731 kB 7.6 MB/s 
Requirement already satisfied: numpy>=1.17.3 in /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages (from pandas>=0.23.0->geopandas) (1.21.2)
Requirement already satisfied: python-dateutil>=2.7.3 in /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages (from pandas>=0.23.0->geopandas) (2.8.2)
Requirement already satisfied: pytz>=2017.3 in /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages (from pandas>=0.23.0->geopandas) (2021.1)
Requirement already satisfied: six>=1.5 in /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/site-packages (from python-dateutil>=2.7.3->pandas>=0.23.0->geopandas) (1.16.0)
Collecting cligj>=0.4
  Downloading cligj-0.7.2-py3-none-any.whl (7.1 kB)
Collecting click-plugins
  Downloading click_plugins-1.1.1-py2.py3-none-any.whl (7.5 kB)
Collecting munch
  Downloading munch-2.5.0-py2.py3-none-any.whl (10 kB)
Collecting click>=4.0
  Using cached click-8.0.1-py3-none-any.whl (97 kB)
Building wheels for collected packages: fiona, pyproj, shapely
  Building wheel for fiona (setup.py) ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_17b126e9b24d4b81991cfffa42c2143b/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_17b126e9b24d4b81991cfffa42c2143b/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-wheel-4p4deu16
       cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_17b126e9b24d4b81991cfffa42c2143b/
  Complete output (50 lines):
  Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
  /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/distutils/dist.py:274: UserWarning: Unknown distribution option: 'metadata_version'
    warnings.warn(msg)
  /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/distutils/dist.py:274: UserWarning: Unknown distribution option: 'requires_python'
    warnings.warn(msg)
  /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/distutils/dist.py:274: UserWarning: Unknown distribution option: 'requires_external'
    warnings.warn(msg)
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.macosx-10.9-x86_64-3.8
  creating build/lib.macosx-10.9-x86_64-3.8/fiona
  copying ./fiona/compat.py -> build/lib.macosx-10.9-x86_64-3.8/fiona
  copying ./fiona/drvsupport.py -> build/lib.macosx-10.9-x86_64-3.8/fiona
  copying ./fiona/inspector.py -> build/lib.macosx-10.9-x86_64-3.8/fiona
  copying ./fiona/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/fiona
  copying ./fiona/crs.py -> build/lib.macosx-10.9-x86_64-3.8/fiona
  copying ./fiona/rfc3339.py -> build/lib.macosx-10.9-x86_64-3.8/fiona
  copying ./fiona/transform.py -> build/lib.macosx-10.9-x86_64-3.8/fiona
  copying ./fiona/collection.py -> build/lib.macosx-10.9-x86_64-3.8/fiona
  copying ./fiona/errors.py -> build/lib.macosx-10.9-x86_64-3.8/fiona
  copying ./fiona/tool.py -> build/lib.macosx-10.9-x86_64-3.8/fiona
  creating build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/options.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/collect.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/distrib.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/env.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/insp.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/cat.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/ls.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/dump.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/calc.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/filter.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/load.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/main.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/info.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/helpers.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  copying ./fiona/fio/bounds.py -> build/lib.macosx-10.9-x86_64-3.8/fiona/fio
  running build_ext
  building 'fiona._transform' extension
  creating build/temp.macosx-10.9-x86_64-3.8
  creating build/temp.macosx-10.9-x86_64-3.8/fiona
  gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/tillmeineke/miniforge3/envs/nf_base/include -arch x86_64 -I/Users/tillmeineke/miniforge3/envs/nf_base/include -arch x86_64 -I/Users/tillmeineke/miniforge3/envs/nf_base/include/python3.8 -c fiona/_transform.cpp -o build/temp.macosx-10.9-x86_64-3.8/fiona/_transform.o
  fiona/_transform.cpp:606:10: fatal error: 'cpl_conv.h' file not found
  #include "cpl_conv.h"
           ^~~~~~~~~~~~
  1 error generated.
  error: command 'gcc' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for fiona
  Running setup.py clean for fiona
  Building wheel for pyproj (setup.py) ... done
  Created wheel for pyproj: filename=pyproj-1.9.6-cp38-cp38-macosx_10_9_x86_64.whl size=3236932 sha256=5e5334d1d4183eb7dc3452aa32a520cfbd5757eb2b6fa99161a0645304531818
  Stored in directory: /Users/tillmeineke/Library/Caches/pip/wheels/88/f9/15/d2091255dc0aad51e9a83ab7293de72c5c42f5241fb8a9828c
  Building wheel for shapely (setup.py) ... done
  Created wheel for shapely: filename=Shapely-1.7.1-cp38-cp38-macosx_10_9_x86_64.whl size=359825 sha256=449a23f7e03221c135d2a6caf0eac25d0dec166516989a293260cf27bdceb3dd
  Stored in directory: /Users/tillmeineke/Library/Caches/pip/wheels/4c/4d/68/cab6197a548a518cac80203c988b13ed114f0c41efd1b4ac47
Successfully built pyproj shapely
Failed to build fiona
Installing collected packages: click, munch, cligj, click-plugins, shapely, pyproj, fiona, geopandas
    Running setup.py install for fiona ... error
    ERROR: Command errored out with exit status 1:
     command: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_17b126e9b24d4b81991cfffa42c2143b/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_17b126e9b24d4b81991cfffa42c2143b/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-record-ybfkpvd1/install-record.txt --single-version-externally-managed --compile --install-headers /Users/tillmeineke/miniforge3/envs/nf_base/include/python3.8/fiona
         cwd: /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_17b126e9b24d4b81991cfffa42c2143b/
    Complete output (20 lines):
    Failed to get options via gdal-config: [Errno 2] No such file or directory: 'gdal-config'
    /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/distutils/dist.py:274: UserWarning: Unknown distribution option: 'metadata_version'
      warnings.warn(msg)
    /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/distutils/dist.py:274: UserWarning: Unknown distribution option: 'requires_python'
      warnings.warn(msg)
    /Users/tillmeineke/miniforge3/envs/nf_base/lib/python3.8/distutils/dist.py:274: UserWarning: Unknown distribution option: 'requires_external'
      warnings.warn(msg)
    running install
    running build
    running build_py
    running build_ext
    building 'fiona._transform' extension
    creating build/temp.macosx-10.9-x86_64-3.8
    creating build/temp.macosx-10.9-x86_64-3.8/fiona
    gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/tillmeineke/miniforge3/envs/nf_base/include -arch x86_64 -I/Users/tillmeineke/miniforge3/envs/nf_base/include -arch x86_64 -I/Users/tillmeineke/miniforge3/envs/nf_base/include/python3.8 -c fiona/_transform.cpp -o build/temp.macosx-10.9-x86_64-3.8/fiona/_transform.o
    fiona/_transform.cpp:606:10: fatal error: 'cpl_conv.h' file not found
    #include "cpl_conv.h"
             ^~~~~~~~~~~~
    1 error generated.
    error: command 'gcc' failed with exit status 1
    ----------------------------------------
ERROR: Command errored out with exit status 1: /Users/tillmeineke/miniforge3/envs/nf_base/bin/python3.8 -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_17b126e9b24d4b81991cfffa42c2143b/setup.py'"'"'; __file__='"'"'/private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-install-6vd_z94y/fiona_17b126e9b24d4b81991cfffa42c2143b/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/r8/zdlnr35s6qz6zx67nmc9bdnm0000gn/T/pip-record-ybfkpvd1/install-record.txt --single-version-externally-managed --compile --install-headers /Users/tillmeineke/miniforge3/envs/nf_base/include/python3.8/fiona Check the logs for full command output.

❯        
```
