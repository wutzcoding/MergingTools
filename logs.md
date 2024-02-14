requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://huggingface.co/api/models/meta-llama/Llama-2-70b-chat-hf/tree/main?recursive=True&expand=False

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/bin/mergekit-moe", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1157, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
  File "/workspace/automerge/mergekit/mergekit/options.py", line 76, in wrapper
    f(*args, **kwargs)
  File "/workspace/automerge/mergekit/mergekit/scripts/mixtral_moe.py", line 453, in main
    build(
  File "/workspace/automerge/mergekit/mergekit/scripts/mixtral_moe.py", line 303, in build
    model.tensor_index(cache_dir=merge_options.transformers_cache),
  File "/workspace/automerge/mergekit/mergekit/common.py", line 134, in tensor_index
    for fn in huggingface_hub.list_repo_files(
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_validators.py", line 118, in _inner_fn
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/hf_api.py", line 2605, in list_repo_files
    return [
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/hf_api.py", line 2605, in <listcomp>
    return [
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/hf_api.py", line 2741, in list_repo_tree
    for path_info in paginate(path=tree_url, headers=headers, params={"recursive": recursive, "expand": expand}):
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_pagination.py", line 36, in paginate
    hf_raise_for_status(r)
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_errors.py", line 302, in hf_raise_for_status
    raise GatedRepoError(message, response) from e
huggingface_hub.utils._errors.GatedRepoError: 401 Client Error. (Request ID: Root=1-65ccd07f-7e502017111634e83adcbbd9;677bc896-1117-486b-a900-d1edbbd4f68f)

Cannot access gated repo for url https://huggingface.co/api/models/meta-llama/Llama-2-70b-chat-hf/tree/main?recursive=True&expand=False.
Repo model meta-llama/Llama-2-70b-chat-hf is gated. You must be authenticated to access it.
Traceback (most recent call last):
  File "/workspace/automerge/automerge70B.py", line 58, in <module>
    generate_and_merge_models()
  File "/workspace/automerge/automerge70B.py", line 54, in generate_and_merge_models
    subprocess.run(["mergekit-moe", "config.yaml", "merge", "--copy-tokenizer", "--allow-crimes",
  File "/usr/lib/python3.10/subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['mergekit-moe', 'config.yaml', 'merge', '--copy-tokenizer', '--allow-crimes', '--out-shard-size', '1B', '--lazy-unpickle', '--device', 'cuda', '--low-cpu-memory', '--trust-remote-code']' returned non-zero exit status 1.
root@542473efa832:/workspace/automerge#


### Logs 2nd machine requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://huggingface.co/api/models/meta-llama/Llama-2-70b-chat-hf/tree/main?recursive=True&expand=False

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/bin/mergekit-moe", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1157, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
  File "/workspace/automerge/mergekit/mergekit/options.py", line 76, in wrapper
    f(*args, **kwargs)
  File "/workspace/automerge/mergekit/mergekit/scripts/mixtral_moe.py", line 453, in main
    build(
  File "/workspace/automerge/mergekit/mergekit/scripts/mixtral_moe.py", line 303, in build
    model.tensor_index(cache_dir=merge_options.transformers_cache),
  File "/workspace/automerge/mergekit/mergekit/common.py", line 134, in tensor_index
    for fn in huggingface_hub.list_repo_files(
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_validators.py", line 118, in _inner_fn
    return fn(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/hf_api.py", line 2605, in list_repo_files
    return [
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/hf_api.py", line 2605, in <listcomp>
    return [
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/hf_api.py", line 2741, in list_repo_tree
    for path_info in paginate(path=tree_url, headers=headers, params={"recursive": recursive, "expand": expand}):
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_pagination.py", line 36, in paginate
    hf_raise_for_status(r)
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_errors.py", line 302, in hf_raise_for_status
    raise GatedRepoError(message, response) from e
huggingface_hub.utils._errors.GatedRepoError: 401 Client Error. (Request ID: Root=1-65ccd07f-7e502017111634e83adcbbd9;677bc896-1117-486b-a900-d1edbbd4f68f)

Cannot access gated repo for url https://huggingface.co/api/models/meta-llama/Llama-2-70b-chat-hf/tree/main?recursive=True&expand=False.
Repo model meta-llama/Llama-2-70b-chat-hf is gated. You must be authenticated to access it.
Traceback (most recent call last):
  File "/workspace/automerge/automerge70B.py", line 58, in <module>
    generate_and_merge_models()
  File "/workspace/automerge/automerge70B.py", line 54, in generate_and_merge_models
    subprocess.run(["mergekit-moe", "config.yaml", "merge", "--copy-tokenizer", "--allow-crimes",
  File "/usr/lib/python3.10/subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['mergekit-moe', 'config.yaml', 'merge', '--copy-tokenizer', '--allow-crimes', '--out-shard-size', '1B', '--lazy-unpickle', '--device', 'cuda', '--low-cpu-memory', '--trust-remote-code']' returned non-zero exit status 1.
root@542473efa832:/workspace/automerge#
